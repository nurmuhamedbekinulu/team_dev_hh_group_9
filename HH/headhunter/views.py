from urllib.parse import urlencode
from django.db.models import Q
from django.views.generic import ListView
from .models import Vacancy


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 20
    model = Vacancy
    context_object_name = 'vacancy'
    