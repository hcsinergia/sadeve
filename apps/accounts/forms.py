from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from apps.accounts.models import Account
from apps.socio.models import Socio





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = (
        	'email', 
        	'username', 
        	'password1', 
        	'password2', 
        	)
	# def save(self, commit=True):
 #    	user = super.(RegistrationForm, self).save(commit=False)
 #    	user.first_name = cleaned_data['first_name']
 #    	user.las_name = cleaned_data['last_name']
 #    	user.email = cleaned_data['email']

 #    	if commit:
 #    		user.save()

 #    	return user


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		if not authenticate(email=email, password=password):
			raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username', )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
















