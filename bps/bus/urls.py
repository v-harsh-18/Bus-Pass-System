from django.urls import path
from . import views

urlpatterns = [
    path('update',views.update),
    path('register',views.register),
    path('login',views.login),
    path('showbus',views.showbus),
    path('track',views.track),
    path('trackbus',views.trackbus),
    path('',views.home),
    path('buslist', views.buslist),
    path('seat', views.seat),
    path('payment',views.payment),
    path('passenger',views.passenger),
    path('topup',views.topup),
    path('book',views.book),
    path('ticket',views.ticket)

]