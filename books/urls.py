from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('list/', views.BookListView.as_view(), name ='home'),
]



