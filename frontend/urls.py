from django.urls import paths

from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
