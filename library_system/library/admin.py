# library/admin.py
from django.contrib import admin
from .models import Department, Subject, Book, Transaction

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Book)
admin.site.register(Transaction)
