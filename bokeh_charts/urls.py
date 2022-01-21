from django.urls import path, include
from .views import home




app_name = 'bokeh_charts'
urlpatterns = [
    path('', home, name='home')
]