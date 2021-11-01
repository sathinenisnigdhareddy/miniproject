from django.urls import path
from . import views
from django.conf.urls import url,include


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('grocery/<str:pk>/', views.grocery, name="grocery"),
	path('home/', views.home, name="home"),
]
