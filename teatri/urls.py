from django.urls import path
from . import views

urlpatterns = [
    path('', views.teatri_list, name='teatri_list'),
    path('profili-<pk>/', views.profili_detail, name='profili_detail'),
    path('<pk>/', views.index, name='index'),
]