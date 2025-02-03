from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('', home, name='home'),  # Root URL
]
