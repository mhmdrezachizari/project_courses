from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterUserView

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='index'),
    path('login/', views.obtain_auth_token)
]