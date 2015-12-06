from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def profile(request):
	title= "Hello"
	context = {
		'title':title
	}
	#if request.user.is_authenticated():
	queryset = User.objects.filter(email=request.user.email).order_by('-id')[:1]  
	#print vars(queryset[0])
	context['queryset'] = queryset[0]
	return render(request,"profile.html",context)
	#return render(request,"home.html")

def home(request):
	title= "Contact Me"
	contactform = ContactForm(request.POST or None)
		
	if contactform.is_valid():
		form_full_name = contactform.cleaned_data.get("full_name")
		form_email = contactform.cleaned_data.get("email")
		form_message = contactform.cleaned_data.get("message")

		subject="Test"
		from_email = settings.EMAIL_HOST_USER
		print from_email
		to_email = ['huynhchanhuy@gmail.com'] # or huynhchanhuy@gmail.com ||| system email to admin@email
		contact_message = "Name: %s: \nMessage:\n%s \nEmail: %s " % (form_full_name,form_message,form_email)
		send_mail(subject,contact_message, from_email,to_email,fail_silently=False)

	context = {
		'title':title,
		'form':contactform
	}
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = SignUp.objects.all
		context['queryset'] = queryset
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)



	return render(request,"home.html",context)