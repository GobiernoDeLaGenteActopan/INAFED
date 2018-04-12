from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login, logout
from main.views import Home

urlpatterns = [
	path('', Home.as_view(), name="home"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('admin/', admin.site.urls),
]
