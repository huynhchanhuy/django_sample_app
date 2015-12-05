from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', 'photofeeds.views.home' ,name="home"),
	url(r'^contact/', 'photofeeds.views.contact' ,name="contact"),
	url(r'^about', 'instagram_clone.views.about' ,name="about"),
	url(r'^admin/', include(admin.site.urls)),
#url(r'^rango/', include('rango.urls')),
#url(r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
	print settings.STATIC_URL
	print settings.MEDIA_URL
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)