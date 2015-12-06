from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# def home(request):
# 	title = 'Welcome !'
# 	#if request.user.is_authenticated():
# 		#title = request.user
# 	#import pprint
# 	#pprint.pprint(vars(request))
# 	#import pdb
# 	#pdb.set_trace()
# 	form = contact(request) #SignUpForm(request.POST or None)
# 	context = {
# 		'title':title,
# 		'form':form
# 	}
# 	if form.is_valid():
# 		#form.save()
# 		instance = form.save(commit = False)
# 		full_name = form.cleaned_data.get("full_name")
# 		if not full_name:
# 			full_name = "Empty"
# 		instance.full_name = full_name
# 		#print full_name
# 		#if not instance.full_name:
# 			#instance.full_name = "Empty"
# 		instance.save()
# 		#print instance.email
# 		#print instance.timestamp
# 		context = {
# 			'title':"Thank You",
# 			#'form':form
# 		}
# 	return render(request,"home.html",context)






def home(request):
	title= "Contact Me"
	form = ContactForm(request.POST or None)
		
	if form.is_valid():
		#for key in form.cleaned_data:
			#print key
			#print form.cleaned_data.get(key)
		form_full_name = form.cleaned_data.get("full_name")
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")

		subject="Test"
		from_email = settings.EMAIL_HOST_USER
		print from_email
		to_email = ['huynhchanhuy@gmail.com'] # or huynhchanhuy@gmail.com ||| system email to admin@email
		contact_message = "%s: %s via %s " % (form_full_name,form_message,form_email)
		send_mail(subject,contact_message, from_email,to_email,fail_silently=False)

	context = {
		'title':title,
		'form':form
	}
	return render(request,"home.html",context)