from django.http import HttpResponse
from django.shortcuts import render

# from .forms import bookform
from .models import books_list, member_list

# Create your views here.

def home(request):
    return render(request,'index.html')



def booklist(request):


    if request.method == "POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        obj=books_list(title=title,author=author)
        obj.save()

    dictbook = {
        'books': books_list.objects.all()
    }

    return render(request,'booklist.html',dictbook)


def members(request):


    dictmember = {
        'members':member_list.objects.all()
    }
    return render(request,'members.html',dictmember)



# def update(request):
#     form = bookform()
#     books = books_list.objects.all()
#     if request.method == "POST":
#         form = bookform(request.POST)
#         if form.is_valid():
#             form.save()
#
#     return render(request,'"update.html')