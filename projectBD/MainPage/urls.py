from django.urls import path

from . import views

app_name = 'MainPage'

urlpatterns = [
    path('', views.index, name='index'),
    # other url patterns here
]
