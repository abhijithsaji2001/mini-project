from django.urls import path
from . import views

urlpatterns = [
    path("login_page", views.login_page, name='login_page'),
    path("sign_up_page", views.sign_up_page, name='sign_up_page'),
    path("logout", views.logout_user, name='logout'),
]