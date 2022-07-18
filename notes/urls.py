from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='LandingPage'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('logout/', views.logout, name='logout')
]
    # path('login/', views.login, name='login'),
    # path('login/signup/', views.signup, name='login2'),
    # path('logout/', views.logout, name='logout'),
    # path('dashboard/upload/dashboard/', views.dashboard)
