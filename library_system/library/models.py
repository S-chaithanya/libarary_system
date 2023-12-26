# library/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Book(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=255)
    date_taken = models.DateField()
    date_returned = models.DateField(null=True, blank=True)
