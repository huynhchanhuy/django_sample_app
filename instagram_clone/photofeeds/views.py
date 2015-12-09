from django.shortcuts import render
from .forms import ContactForm,UploadForm,CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import Image,Tag,ImageComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import re


def profile(request,user):
	if request.user.is_authenticated():
		context = {}
		queryset = User.objects.filter(username=user).order_by('-id')[:1] 
		context['queryset'] = queryset[0]
		return render(request,"profile.html",context)
	return HttpResponseRedirect('/accounts/login')



def home(request,page=1):
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

		if request.method == 'GET':
			paginator = Paginator(photofeeds, settings.FEEDS_PER_PAGE)
			try:
				photofeeds = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				photofeeds = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				photofeeds = paginator.page(paginator.num_pages)

		context['previous_page_number'] = photofeeds.previous_page_number
		context['next_page_number'] = photofeeds.next_page_number
		context['has_previous'] = photofeeds.has_previous
		context['has_next'] = photofeeds.has_next
		context['number'] = photofeeds.number
		context['paginator'] = photofeeds.paginator
		context['photofeeds'] = []
		for img in photofeeds:
			context['photofeeds'].append({'img':img,'comments':ImageComment.objects.filter(image=img).order_by('-created')})

		context['mediaurl'] = settings.MEDIA_URL
		return render(request,view,context)


	return render(request,view,context)

def collectTags(img):
	text = img.title
	taglist=getTags(text)
	for tag in taglist:
		res=Tag.objects.filter(tag=tag)
		if res.count() > 0:
			res=res[0]
		else:
			savetag=Tag(tag=tag)
			savetag.save()
			res = savetag
		img.tags.add(res)
		text=re.sub("#%s"%tag,"<a href=\""+reverse('tags', args=(), kwargs={'hashtag':tag})+"\">#"+tag+"</a>",text)
	img.title = text
	return img

def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			uploadimage = form.save(commit=False)
			uploadimage.user = request.user
			uploadimage.save()
			uploadimage = collectTags(uploadimage)
			uploadimage.save()
			url = reverse('home', args=(), kwargs={})
			return HttpResponseRedirect(url)
	return render(request,'imageupload.html')


def submitcomment(request):
	
	payload={'success':True}

	if request.is_ajax() and request.method == 'POST':
		image_model = Image.objects.filter(imghash=request.POST.get('value[2][value]', ''))[:1][0]
		comment = request.POST.get('value[1][value]', '')
		taglist=getTags(comment)
		for tag in taglist:
			res=Tag.objects.filter(tag=tag)
			#print tag
			if res.count() > 0:
				res = res[0]
			else:
				savetag=Tag(tag=tag)
				savetag.save()
				res = savetag
				#image.tags.add(savetag)
			image_model.tags.add(res)

			comment=re.sub("#%s"%tag,"<a href=\""+reverse('tags', args=(), kwargs={'hashtag':tag})+"\">#"+tag+"</a>",comment)
			#comment=re.sub("#%s"%tag,"<a href=\"{% url 'tags'"+tag+" %}\"/"+tag+"/>#"+tag+"</a>",comment)
		#tags = image_model.tags.all().exclude(tag__in=list([taglist]))
		payload['comment'] = comment
		# for tag in tags:
		# 	print tag
		# 	image_model.tags.add(tag)
			
		comment_model = ImageComment(comment=comment,user=request.user,image=image_model)
		comment_model.save()

	return HttpResponse(json.dumps(payload), content_type='application/json')

def tags(request,hashtag,page=1):
	if request.user.is_authenticated():
		context={}
		commentform = CommentForm(request.POST or None)
		context['commentform'] = commentform
		if commentform.is_valid():
			commentform.save(commit=False)
		res=Tag.objects.filter(tag=hashtag)
		print res
		photofeeds = Image.objects.filter(tags__id=res[0].id).order_by('-created').all()
		print hashtag
		if request.method == 'GET':
			paginator = Paginator(photofeeds, settings.FEEDS_PER_PAGE)
			try:
				photofeeds = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				photofeeds = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				photofeeds = paginator.page(paginator.num_pages)

		context['previous_page_number'] = photofeeds.previous_page_number
		context['next_page_number'] = photofeeds.next_page_number
		context['has_previous'] = photofeeds.has_previous
		context['has_next'] = photofeeds.has_next
		context['number'] = photofeeds.number
		context['paginator'] = photofeeds.paginator
		context['photofeeds'] = []
		for img in photofeeds:
			context['photofeeds'].append({'img':img,'comments':ImageComment.objects.filter(image=img).order_by('-created')})

		context['mediaurl'] = settings.MEDIA_URL
		return render(request,'photofeeds.html',context)

	return HttpResponseRedirect(reverse('home', args=(), kwargs={}))

def getTags(comment):
	return {tag[1:] for tag in comment.split() if tag.startswith("#") and not re.match("#" ,tag[1:])}