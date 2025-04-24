from django.contrib import admin
from django.urls import path, include
from django.urls import path  # ← 반드시 include 추가!


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/chat/', include('chat.urls')),
]
