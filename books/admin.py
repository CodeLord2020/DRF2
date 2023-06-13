from django.contrib import admin
from .models import Book, Todo, TodoAdmin
# Register your models here.


admin.site.register(Book)
admin.site.register(Todo, TodoAdmin)