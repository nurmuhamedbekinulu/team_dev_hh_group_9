from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Vacancy
from .forms import VacancyForm
from django.urls import reverse
from django.utils import timezone


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 20
    model = Vacancy
    context_object_name = 'vacancy'

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
