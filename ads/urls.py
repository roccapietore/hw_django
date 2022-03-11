from django.urls import path
from ads import views

urlpatterns = [
    path('ad/',  views.AdListView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('create_ad/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image', views.AdImageView.as_view()),

    path('cat/', views.CategoryListView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('create_cat/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete', views.CategoryDeleteView.as_view()),
    ]



