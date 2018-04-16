from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout
from main.views import Home
from indicadores import urls as indicadoresUrl
from indicadores.views import Dashboard

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('indicadores/', include(indicadoresUrl, namespace="indicadores")),
    path('admin/', admin.site.urls),
]
