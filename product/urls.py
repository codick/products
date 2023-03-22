from django.urls import path
from views import ProductView

urlpatterns = [
    path('', ProductView.as_view(), name="product_view"),
    path('<int:pk>/', ProductView.as_view(), name="product_view"),
]
