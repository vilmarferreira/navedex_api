"""navedex_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from navers.views import NaversViewSet
from projects.views import ProjectViewSet
from users.views import RegisterView
from rest_framework import routers

ROUTER = routers.SimpleRouter(trailing_slash=False)
ROUTER.register('navers',NaversViewSet)
ROUTER.register('projects',ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-register/", RegisterView.as_view()),
    path("api-token-auth/", obtain_jwt_token),
    path("api-token-verify/", verify_jwt_token),
    path("api-token-refresh/", refresh_jwt_token),
    path("api/v1/", include((ROUTER.urls, "navedex_api"), namespace="v1")),
]
