from django.db import models

# Create your models here.

class books_list(models.Model):
    title = models.CharField(max_length=110)
    author = models.TextField()

    def __str__(self):
        return self.title


class member_list(models.Model):
    name=models.CharField(max_length=160)
    bookname=models.ForeignKey(books_list, on_delete=models.CASCADE)
    borrowedon = models.DateField(auto_now=True)
    borrowdate = models.DateField()
    def __str__(self):
        return self.name