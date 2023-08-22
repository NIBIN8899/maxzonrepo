from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('book', views.booklist, name='booklist'),
    path('members', views.members, name='members'),
    # path('update', views.update, name='update')

]