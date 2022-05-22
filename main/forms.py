from django import forms
from django.forms import PasswordInput

from .models import Question, Customer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'email', 'content')
        widgets = {'content': forms.Textarea()}
        labels = {"name": "Имя", "email": "Адрес электронной почты", "content": "Вопрос"}


class UserReg(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=PasswordInput)
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=Customer.genders, label="Пол")
