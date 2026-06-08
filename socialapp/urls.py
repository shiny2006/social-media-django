from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.feed,
        name='feed'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    path(
        'delete/',
        views.delete_account,
        name='delete'
    )

]