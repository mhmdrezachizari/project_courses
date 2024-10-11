from django.urls import path
from .views import CustomAdmin
app_name = 'customAdmin'
urlpatterns = [
    path('' , CustomAdmin.as_view())
]