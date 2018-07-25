from django.urls import path
from .views import indicadoresListView, indicadoresDetailView, SatisfactorioList, RegularList, PesimoList, ResumenAreaDetail, ResumenAreaList, ResumenGeneral
app_name="indicadores"

urlpatterns = [
    path('', indicadoresListView.as_view(), name="list"),
    path('satisfactorio/', SatisfactorioList.as_view(), name="satisfactorio"),
    path('regular/', RegularList.as_view(), name="regular"),
    path('pesimo/', PesimoList.as_view(), name="pesimo"),
    path('<int:pk>/', indicadoresDetailView.as_view(), name="detail"),
    path('resumen/seleccionar_area/', ResumenAreaList.as_view(), name="resumen_area_list" ),
    path('resumen/general/', ResumenGeneral.as_view(), name="resumen_general"),
    path('resumen/<str:username>/', ResumenAreaDetail.as_view(), name="resumen_area_detail"),
    #path('<int:pk>/evidencias/<int:epk>/', EvidenciasDetailView.as_view(), name="evidencia_det"),

]