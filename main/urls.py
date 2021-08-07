
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/login_user', views.login_user),
    path('user/dashboard', views.dashboard),
    path('user/logout_user', views.logout_user),
    path('lure/lure_form', views.lure_form),
    path('lure/create_location', views.create_location),
    path('lure/best_lures/<int:id>', views.best_lures),
]