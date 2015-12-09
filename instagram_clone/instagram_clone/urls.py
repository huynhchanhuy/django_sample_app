from django.conf.urls import patterns, include, url
from django.contrib import admin #declare admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', 'photofeeds.views.home' ,name="home"),
	url(r'^page/(?P<page>[0-9]+)/$','photofeeds.views.home', name="home"),
	url(r'^upload/$', 'photofeeds.views.upload' ,name="upload"),
	url(r'^tags/(?P<hashtag>\w{0,32})/', 'photofeeds.views.tags' ,name="tags"),
	url(r'^tags/(?P<hashtag>\w{0,32})/(?P<page>[0-9]+)/', 'photofeeds.views.tags' ,name="tags"),
	url(r'^submitcomment/$', 'photofeeds.views.submitcomment' ,name="submitcomment"),
	url(r'^followby/(?P<user>\w{0,32})/', 'photofeeds.views.followby' ,name="followby"),
	url(r'^profile/(?P<user>\w{0,32})/', 'photofeeds.views.profile' ,name="profile"),
	url(r'^profile/(?P<user>\w{0,32})/(?P<page>[0-9]+)', 'photofeeds.views.profile' ,name="profile"),
	url(r'^admin/', include(admin.site.urls)), #set admin
	url(r'^accounts/',include('registration.backends.default.urls')),
	#url(r'^comments/', include('django_comments.urls')),
#url(r'^rango/', include('rango.urls')),
#url(r'^accounts/', include('registration.backends.simple.urls')),
)

# print settings.DEBUG
# print settings.DATABASES

if settings.DEBUG:
	# print settings.STATIC_URL
	# print settings.MEDIA_URL
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)