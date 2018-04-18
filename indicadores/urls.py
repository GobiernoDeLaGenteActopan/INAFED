from django.urls import path
from .views import indicadoresListView, indicadoresDetailView, SatisfactorioList, RegularList, PesimoList

app_name="indicadores"

urlpatterns = [
    path('', indicadoresListView.as_view(), name="list"),
    path('satisfactorio/', SatisfactorioList.as_view(), name="satisfactorio"),
    path('regular/', RegularList.as_view(), name="regular"),
    path('pesimo/', PesimoList.as_view(), name="pesimo"),
    path('<int:pk>/', indicadoresDetailView.as_view(), name="detail"),
]