from django.shortcuts import render
from .forms import ContactForm,UploadForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Image

def profile(request):
	title= "Hello"
	context = {
		'title':title
	}
	#if request.user.is_authenticated():
	queryset = User.objects.filter(email=request.user.email).order_by('-id')[:1]  
	context['queryset'] = queryset[0]
	return render(request,"profile.html",context)

def home(request):
	title= "Contact Me"
	view = "home.html"
	contactform = ContactForm(request.POST or None)
	context = {
			'title':title,
			'contactform':contactform
	}
	if contactform.is_valid():
		form_full_name = contactform.cleaned_data.get("full_name")
		form_email = contactform.cleaned_data.get("email")
		form_message = contactform.cleaned_data.get("message")

		subject="Test"
		from_email = settings.EMAIL_HOST_USER
		#print from_email
		to_email = ['huynhchanhuy@gmail.com'] # or huynhchanhuy@gmail.com ||| system email to admin@email
		contact_message = "Name: %s: \nMessage:\n%s \nEmail: %s " % (form_full_name,form_message,form_email)
		send_mail(subject,contact_message, from_email,to_email,fail_silently=False)

	if request.user.is_authenticated():
		view = "photofeeds.html"
		photofeeds = Image.objects.all()
		context['photofeeds']=photofeeds
		context['mediaurl'] = settings.MEDIA_URL
		return render(request,view,context)
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)



	return render(request,view,context)

def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			#m = Image.objects.get(pk=course_id)
			# title = form.cleaned_data['title']
			# print title
			form.save()
			url = reverse('home', args=(), kwargs={})
			return HttpResponseRedirect(url)
	return render(request,'imageupload.html')