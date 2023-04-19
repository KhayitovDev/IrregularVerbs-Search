from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page, name='search_page' ),
    path('detail/<int:pk>/', views.detail_page, name='detail_page')
]
