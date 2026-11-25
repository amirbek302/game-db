"""
URL configuration for game_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from games import views as game_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/game_db/', game_views.GamesListAPIView.as_view()),
    path('api/v1/category/', game_views.CategoryListAPIView.as_view()),
    path('api/v1/price/', game_views.PriceListAPIView.as_view()),

    path('api/v1/game_db/<int:pk>', game_views.GameDetailAPIView.as_view()),

    path('api/v1/game_db/delete/<int:pk>', game_views.GameDeleteAPIView.as_view()),
    path('api/v1/category/delete/<int:pk>', game_views.CategoryDeleteAPIView.as_view()),
    path('api/v1/price/delete/<int:pk>', game_views.PriceDeleteAPIView.as_view()),
]
