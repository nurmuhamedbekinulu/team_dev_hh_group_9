from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Vacancy, Resume, Response, Message
from .forms import VacancyForm, ResumeForm, ResponseForm
from django.urls import reverse
from django.utils import timezone


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 20
    model = Vacancy
    context_object_name = 'vacancy'
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.user_role == 'Employer':
                queryset = Resume.objects.filter(is_active=True).order_by('-updated_at')
            else:
                queryset = Vacancy.objects.filter(is_active=True).order_by('-updated_at')
        return queryset

class VacancyCreate(CreateView):
    template_name = "vacancy_create.html"
    form_class = VacancyForm
    model = Vacancy

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.author_id})    
    
class VacancyDetail(DetailView):
    template_name = "vacancy_detail.html"
    model = Vacancy
    context_object_name = "vacancy"
    
    
class VacancyUpdate(UpdateView):
    template_name = "vacancy_update.html"
    form_class = VacancyForm
    model = Vacancy

    def get_success_url(self):
        return reverse('vacancy_detail', kwargs={'pk': self.object.pk})


def vacancy_renew(request, *args, **kwargs):
    vacancy = get_object_or_404(Vacancy, pk=kwargs['pk'])
    vacancy.updated_at = timezone.now()
    vacancy.save()

    return redirect('vacancy_detail', pk=kwargs['pk'])


class ResumeCreate(CreateView):
    model = Resume

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('resume_update', pk=resume.pk)


class ResumeUpdate(UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_update.html'
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super(ResumeUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.author_id})
    
    
class ResumeDetail(DetailView):
    model = Resume
    template_name = "resume_detail.html"
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy'] = Vacancy.objects.filter(author=self.request.user)
        context['response_form'] = ResponseForm(current_user=self.request.user)
        return context
    
    
def resume_renew(request, *args, **kwargs):
    resume = get_object_or_404(Resume, pk=kwargs['pk'])
    resume.updated_at = timezone.now()
    resume.save()

    return redirect('resume_detail', pk=kwargs['pk'])

class AddResponseView(CreateView):
    model = Response

    def post(self, request, *args, **kwargs):
        for response in Response.objects.all():
            if response.resume.pk == int(request.POST['resume']) and response.vacancy.pk == int(
                    request.POST['vacancy']):
                return HttpResponseBadRequest('error')
        result = Response.objects.create(vacancy_id=request.POST['vacancy'], resume_id=request.POST['resume'])
        Message.objects.create(message=result, user=request.user, text=request.POST['message'])
        return HttpResponse('success')
    
    
class ResponseList(ListView):
    model = Response
    template_name = 'user_response.html'
    context_object_name = 'responses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
   
   
class  CreateMessageToResponse(CreateView):
    def post(self, request, *args, **kwargs):
        response = get_object_or_404(Response, pk=kwargs['pk'])
        Message.objects.create(message=response, user=request.user, text=request.POST['message'])
        return redirect('response_list')
