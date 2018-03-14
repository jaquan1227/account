from django.urls import path

from . import views

app_name = 'account_app'

urlpatterns = [
    path('login/', views.RidiLoginView.as_view(), name='login'),
]