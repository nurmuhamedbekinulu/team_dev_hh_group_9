from django import forms

from .models import Vacancy, Resume, CATEGORY


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'salary', 'description', 'experience', 'category', 'is_active']
   
class ResumeForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY, label='Категория вакансии', required=True)
    telegram = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Введите ссылку на телеграм', 'class': "form-control"}))
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Введите почту', 'class': "form-control"}))
    phone_number = forms.CharField(required=True, label='номер телефона', widget=forms.TextInput(
        attrs={'placeholder': 'Введите номер телефона', 'class': "form-control"}))

    class Meta:
        model = Resume
        fields = ('name', 'category', 'about', 'salary', 'telegram', 'email', 'phone_number', 'linkedin', 'facebook')
        required_fields = ['category', 'telegram', 'email', 'phone_number']
     