from django.contrib import admin
from .models import books_list, member_list
# Register your models here.

admin.site.register(books_list)
admin.site.register(member_list)