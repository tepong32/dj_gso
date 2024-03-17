from django.contrib import admin
from .models import Category, SubCategory, Asset

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Asset)
