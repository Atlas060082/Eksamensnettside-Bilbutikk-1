from django.urls import path
from . import views

app_name = 'biler'

urlpatterns = [
    path('', views.oversikt, name='oversikt'),
    path('bil/<int:bil_id>/', views.bildetaljer, name='bildetaljer'),
    path('servicer/', views.serviceoversikt, name='serviceoversikt'),
]