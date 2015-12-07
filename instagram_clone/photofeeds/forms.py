# from .models import SignUp
from django import forms
from .models import Image

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField(widget = forms.Textarea())

class UploadForm(forms.ModelForm):
	# image = forms.ImageField()
	# title = forms.CharField(max_length=60)
	class Meta:
		model = Image
		fields = ['image','title','user']
	def clean_title(self):
		title = self.cleaned_data.get('title')
		# to do validation
		return title

# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['email','full_name']

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base,provider = email.split('@')
# 		domain,extension = provider.split('.')
# 		#if not "edu" in email:
# 		if not extension == 'edu':
# 			raise forms.ValidationError("Please use the valid .edu email")
# 		return email

# 	def clean_full_name(self):
# 		full_name = self.cleaned_data.get('full_name')
# 		# to do validation
# 		return full_name