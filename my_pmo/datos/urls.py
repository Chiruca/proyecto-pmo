from django.urls import path
from . import views

app_name = 'datos'  # Es buena práctica definir un app_name

urlpatterns = [
    path('rep_all/<str:tipo>', views.tablas_view, name='tablas_views'),
    path('rep_roles/<str:tipo>', views.roles_view, name='roles_views'),
    path('detail_rol/<int:id>', views.rol_detail, name='rol_detail'),
    path('detail_marco/<str:tipo>', views.marco_detail, name='metodolog_detail'),
    path('rep_domdes/', views.domdes_view, name='domdes_view'),
    path('detail_domdes/<int:id>', views.domdes_detail, name='domdes_detail'),
    path('rep_domdescoment/<int:id>', views.domdescoment_view, name='domdescoment_view'),
    # path('detail_domdescoment/<int:id>', views.domdescoment_detail, name='domdes_detail'),
    path('rep_metodos/<str:tipo>', views.metodos_view, name='metodos_view'),
    path('detail_metodo/<int:id>', views.metodo_detail, name='metodo_detail'),
]