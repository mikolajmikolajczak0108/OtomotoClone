from django.urls import path

from . import views

app_name = 'MainPage'

urlpatterns = [
    path('', views.index, name='index'),
    path('filter', views.filter_cars, name='filter_cars'),
path('filtered_offers', views.filter_offers, name='filter_offers'),
    # other url patterns here
]
