





from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name = 'my_view'),
    path('htmll/', views.my_html, name = 'my_html'),
    path('db/', views.dbtest, name = 'dbtest'),
]
