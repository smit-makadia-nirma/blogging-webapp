from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(disabled = True)

	class Meta:
		model = User
		fields = ['username', 'email']

class DateInput(forms.DateInput):
	input_type = 'date'

class ProfileUpdateForm(forms.ModelForm):
	birth_date = forms.DateField(widget=DateInput)
	class Meta:
		model = Profile
		fields = ['birth_date','image','id_card']