from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pre_pageant/<int:pk>/', views.pre_pageant_detail, name='pre_pageant_detail'),
    path('pre_pageant/<int:pk>/edit/', views.pre_pageant_edit, name='pre_pageant_edit'),
    path('pre_pageant/add', views.pre_pageant_add, name='pre_pageant_add')
]