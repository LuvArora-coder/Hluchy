from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('videoconf/', views.videoconf, name='videoconf'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('animation/', views.animation_view, name='animation'),
    path('', views.home_view, name='home'),
    path('animation/', views.animation_view, name='animation')
]
