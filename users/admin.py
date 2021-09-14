from django.contrib import admin
from .models import Resume, Education, Experience
# Register your models here.

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Resume)