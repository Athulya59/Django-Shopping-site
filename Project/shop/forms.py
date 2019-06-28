from django import forms
from .models import Users,Login

class PostForm(forms.ModelForm):
	class Meta:
		model=Users
		fields=('username','email','password',)

class GetForm(forms.ModelForm):
	class Meta:
		model=Login
		fields=('username','password',)

