from django.contrib import admin
from .models import PageUser, Course, Lesson, Question

# Register your models here.
admin.site.register(PageUser)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question)