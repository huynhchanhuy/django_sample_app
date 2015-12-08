from django.contrib import admin
from .models import *
# from .forms import SignUpForm

# class SignUpAdmin(admin.ModelAdmin):
# 	pass
	# list_display = ["__unicode__","timestamp","updated"]
	# form = SignUpForm
	# class Meta:
	# 	model = SignUp

# admin.site.register(SignUp,SignUpAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "title", "user", "size", "thumbnail_",
                    "created"]
    list_filter = ["user"]

    def save_model(self, request, obj, form, change):
        if not obj.user: obj.user = request.user
        obj.save()

class ImageCommentAdmin(admin.ModelAdmin):
    list_display = ["comment"]

# class ImageCommentAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__","tags_","image","comment","created"]
#     list_filter = ["tags"]

admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageComment, ImageCommentAdmin)
# admin.site.register(ImageComment, ImageCommentAdmin)