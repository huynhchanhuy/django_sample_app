from django.shortcuts import render
from .forms import ContactForm,UploadForm,CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import Image,Tag
from django_comments.models import Comment
import json
from django.db.models import Q


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
		commentform = CommentForm(request.POST or None)
		context['commentform'] = commentform
		if commentform.is_valid():
			commentform.save(commit=False)

		photofeeds = Image.objects.order_by('-created').all()
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
			uploadimage = form.save(commit=False)
			uploadimage.user = request.user
			# title = form.cleaned_data['title']
			# print title
			uploadimage.save()
			url = reverse('home', args=(), kwargs={})
			return HttpResponseRedirect(url)
	return render(request,'imageupload.html')


def submitcomment(request):
	
	payload={'success':True}

	if request.is_ajax() and request.method == 'POST':
		image = Image.objects.filter(imghash=request.POST.get('value[2][value]', ''))[:1] [0]
		taglist=getTags(request.POST.get('value[1][value]', ''))
		#print tagstack
		#print image.tags.all().exclude(tag__in=list(["duoc","test"])).count()
		for tag in taglist:
			res=Tag.objects.filter(tag=tag)
			#print tag
			if res.count() > 0:
				#print 'yes'
				pass
			else:
				#print 'no'
				savetag=Tag(tag=tag)
				savetag.save()
				#image.tags.add(savetag)
		
		tags = image.tags.all().exclude(tag__in=list([taglist]))
		for tag in tags:
			image.tags.add(savetag)
		#imgtag = Image.objects.filter().exclude(tags__in=["duoc","save"])
		#print imgtag[0]
			#comment=re.sub("#%s"%tag,"<a href=\"{% url 'tags' %}\"/"+tag+"/>#"+tag+"</a>",comment)
		#image.add
		#print request.POST.get('value[1][value]', '')
		#print vars(image[0])
		#form = UploadForm(request.POST, request.FILES)

	return HttpResponse(json.dumps(payload), content_type='application/json')

def tags(request):
	view="tags.html"
	context={}
	return render(request,view,context)

def getTags(comment):
	import re
	print comment
	return {tag[1:] for tag in comment.split() if tag.startswith("#") and not re.match("#" ,tag[1:])}