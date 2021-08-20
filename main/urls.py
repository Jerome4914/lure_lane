
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/login_user', views.login_user),
    path('user/dashboard', views.dashboard),
    path('user/logout_user', views.logout_user),
    path('lure/best_lure_form', views.best_lure_form),
    path('lure/lure_form', views.lure_form),
    path('lure/create_lure', views.create_lure),
    # path('lure/create_location', views.create_location),
    path('lure/best_lures', views.best_lures),
    path('lure/<int:review_id>/edit', views.lure_edit),
    path('lure/<int:review_id>/edit_form', views.edit_form),
    path('review/<int:review_id>/delete', views.delete_review),
]