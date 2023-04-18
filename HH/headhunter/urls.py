from django.urls import path
from .views import IndexView, VacancyCreate

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('vacancy/create', VacancyCreate.as_view(), name='add_vacancy'),
]