from django import forms

from .models import Vacancy, Resume, CATEGORY, Response


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
     
     
class ResponseForm(forms.ModelForm):

    def __init__(self, current_user, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['vacancy'].queryset = self.fields['vacancy'].queryset.filter(author=current_user.pk)

    message = forms.CharField(max_length=3000, required=True, label='Приветственное сообщение ',
                              widget=forms.Textarea(attrs={'name': 'body', 'rows': 10, 'cols': 70}))
    vacancy = forms.ModelChoiceField(
        label='Необходимо выбрать вакансию',
        queryset=Vacancy.objects.all(),
    )

    class Meta:
        model = Response
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        fields = ('message', 'vacancy', )