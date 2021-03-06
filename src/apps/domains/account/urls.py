from django.urls import path

from . import views

app_name = 'account_app'

urlpatterns = [
    path('login/', views.RidiLoginView.as_view(), name='login'),
    path('me/', views.RidiAccountInfoView.as_view(), name='account-info'),

    path('users/', views.UserInfoView.as_view(), name='user'),
    path('users/histories/', views.UserModifiedHistoryView.as_view(), name='user-history'),
]
