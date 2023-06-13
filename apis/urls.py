from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.BookAPIView.as_view(), name="book_list"),
    path("<int:pk>", views.BookDetailView.as_view(), name = "book_detail"),
    path("API_RUD/<int:pk>", views.BookRUDAPIView.as_view(), name = "book_RUD")

]



