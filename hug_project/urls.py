"""hug_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from hug_project_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('detail/', views.about, name='detail'),
    path('detail/tree/<int:id>/', views.tree_detail, name='tree_detail'),
    #path('detail/park/<int:id>/', views.park_detail, name='park_detail'),
    #path('detail/food_tree/<int:id>/', views.food_tree_detail, name='food_tree_detail'),
    path('favourites/', views.favourites, name='favourites'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# WHen deploying need to chang static stuff see here for info:
# https://docs.djangoproject.com/en/2.0/howto/static-files/deployment/
