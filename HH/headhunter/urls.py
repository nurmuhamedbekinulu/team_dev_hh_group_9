from django.urls import path
from .views import IndexView, VacancyCreate, VacancyDetail, VacancyUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('vacancy/add', VacancyCreate.as_view(), name='add_vacancy'),
    path('vacancy/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/update/<int:pk>', VacancyUpdate.as_view(), name='vacancy_update'),
]