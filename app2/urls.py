from app2.views import display2
from django.urls import path
app_name='app2'
urlpatterns= [
    path('display2/',display2,name='display2'),
]