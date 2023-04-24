from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page, name='search_page' ),
    path('login/', views.Login.as_view(), name='login' ),
    path('admin-view/', views.admin, name='admin-view' ),
    path('create/', views.Create.as_view(),name='create'),
    path('update/<int:pk>/', views.Update.as_view(),name='update'),
    path('delete/<int:pk>/', views.Delete_View.as_view(),name='delete'),
    path('detail/<int:pk>/', views.detail_page, name='detail_page')
]
