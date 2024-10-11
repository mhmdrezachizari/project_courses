from django.urls import path
from .views import AddToCartView ,RemoveFromCartView , CartView ,PaymentView
urlpatterns = [
    path('add/<int:pk>/', AddToCartView.as_view()),
    path('delete/<int:pk>/', RemoveFromCartView.as_view()),
    path('carts/', CartView.as_view() ),
    path('payments/', PaymentView.as_view() ),

]