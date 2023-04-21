from django.urls import path
from .views import RegisterView, LoginView, logout_view, UserDetailView, UserChangeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', UserDetailView.as_view(), name='user_profile'),
    path('change_profile/<int:pk>', UserChangeView.as_view(), name='user_update'),

]
