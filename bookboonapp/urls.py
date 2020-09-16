from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bookboonapp import views

urlpatterns = [
  path('books/', views.BookList.as_view()),
  path('books/<int:pk>/', views.BookDetail.as_view())
]