from django.urls import path
from . import views

app_name = 'evaluacion'

urlpatterns = [
    #evaluacion_ptf views
    path('proyectos/', views.evaluacionPTF_list, name='evaluacionPTF_list'),
    path('proyectos/<int:pk>/', views.evaluacionPTF_detail, name='evaluacionPTF_detail'),
    path('proyectos/evaluar/', views.evaluacionPTF_create, name='evaluacionPTF_create'),
    path('proyectos_delete/<int:pk>/', views.evaluacionPTF_delete, name='evaluacionPTF_delete'),
    path('proyectos_edit/<int:pk>/',views.evaluacionPTF_edit, name='evaluacionPTF_edit'),
]