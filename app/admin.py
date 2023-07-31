from django.contrib import admin

from app.models import Subject, Semester, Section, Degree, Profile

# Register your models here.


admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Degree)
admin.site.register(Profile)
