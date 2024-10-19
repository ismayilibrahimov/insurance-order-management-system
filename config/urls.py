from django.contrib import admin
from django.urls import path
from users.api import UserSignUpView, UserLoginView
from orders.api import OrderListView, OrderCreateView, OrderStatusView
from products.api import ProductListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/signup/', UserSignUpView.as_view(), name='signup'),
    path('api/v1/login/', UserLoginView.as_view(), name='login'),
    path('api/v1/products/', ProductListView.as_view(), name='product-list'),
    path('api/v1/orders/', OrderListView.as_view(), name='order-list'),
    path('api/v1/order/create/', OrderCreateView.as_view(), name='order-create'),
    path('api/v1/order/<int:pk>/status/', OrderStatusView.as_view(), name='order-status'),
]
