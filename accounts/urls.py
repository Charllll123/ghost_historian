from django.urls import path
from . import views

urlpatterns = [
    path('createuser/', views.Create.as_view(), name='createuser'),  
]
