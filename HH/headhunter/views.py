from urllib.parse import urlencode
from django.db.models import Q
from django.views.generic import ListView, CreateView
from .models import Vacancy
from .forms import VacancyForm
from django.urls import reverse


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
    