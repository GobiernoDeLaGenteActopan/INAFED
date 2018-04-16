from django.urls import path
from .views import indicadoresListView, indicadoresDetailView

app_name="indicadores"

urlpatterns = [
    path('', indicadoresListView.as_view(), name="list"),
    path('<int:pk>/', indicadoresDetailView.as_view(), name="detail"),
]