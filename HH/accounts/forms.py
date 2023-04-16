from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, required=True, label='Логин')
    password = forms.CharField(max_length=70, required=True, label='Пароль', widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', required=True, strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвержение пароля', required=True, strip=False, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'phone_number', 'password', 'password_confirm', 'username', 'user_role', 'avatar')
        widgets = {
            'user_role': forms.RadioSelect
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
