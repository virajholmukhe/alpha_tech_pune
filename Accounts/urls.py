from django.urls import path

from . import views



urlpatterns = [
    path('login',views.login),
    path('register',views.register),
    path('logout',views.logout),
    path("forget-password",views.forgetPass),
    path("change-password/<token>",views.checkToken),

]
