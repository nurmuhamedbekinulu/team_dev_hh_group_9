from django.urls import path
from .views import *



urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('vacancy/add', VacancyCreate.as_view(), name='add_vacancy'),
    path('vacancy/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/update/<int:pk>', VacancyUpdate.as_view(), name='vacancy_update'),
    path('vacancy/renew/<int:pk>', vacancy_renew, name='vacancy_renew'),
    path('resume/update/<int:pk>', ResumeUpdate.as_view(), name='resume_update'),
    path('resume/add', ResumeCreate.as_view(), name='add_resume'),
    path('resume/<int:pk>', ResumeDetail.as_view(), name='resume_detail'),
    path('resume/renew/<int:pk>', resume_renew, name='resume_renew'),
    path('responces', ResponseList.as_view(), name='response_list'),
    path('resume/responces/add', AddResponseView.as_view(), name='response_add'),
    path('send/message/<int:pk>', CreateMessageToResponse.as_view(), name='send_message'),
]