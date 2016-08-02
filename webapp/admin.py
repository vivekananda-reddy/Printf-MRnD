from django.contrib import admin

# Register your models here.
from webapp.models import Tour, Picture

admin.site.register([Tour,Picture])