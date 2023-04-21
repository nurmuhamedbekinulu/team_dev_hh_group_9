from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from accounts.forms import LoginForm, RegisterForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from headhunter.models import Vacancy, Resume


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('/')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('/')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('/')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        context = {'form': form}
        return self.render_to_response(context)

    def get_success_url(self):
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


class UserDetailView( DetailView):
    model = get_user_model()
    template_name = "user_profile.html"
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['vacancy'] = Vacancy.objects.filter(author=user).order_by('-updated_at')
        context['resumes'] = Resume.objects.filter(author=user).order_by('-updated_at')
        context['change_form'] = UserChangeForm(instance=self.object)
        return context


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_profile.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.pk})
