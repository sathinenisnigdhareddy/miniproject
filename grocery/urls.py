from django.urls import path
from . import views
from django.conf.urls import url,include


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('grocery/<str:pk>/', views.grocery, name="grocery"),
	path('home/', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
	path('result/<int:pk>/', views.result, name="result"),
 
    path("login/", views.login_request, name="login"),
	
]
