from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='payment'),
	path('paymenthandler/', views.paymenthandler, name='paymenthandler')
]