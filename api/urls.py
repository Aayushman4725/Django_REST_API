from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list),
    path('blog/<int:pk>/', views.blog_detail),
    path('blog_update/<int:pk>/', views.blog_update),
    path('blog_delete/<int:pk>/', views.blog_delete),
    path('blog_add/', views.blog_post),

]