from app1.views import display
from django.urls import path
app_name='app1'
urlpatterns=[
    path('display/',display,name='display'),
]