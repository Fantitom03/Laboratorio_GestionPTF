from django.urls import path
from . import views

app_name = 'evaluacion'

urlpatterns = [
    #evaluacion_ptf views
    path('proyectos/', views.evaluacionPTF_list, name='proyecto_list'),
    path('proyectos/<int:pk>/', views.evaluacionPTF_detail, name='proyecto_detail'),
    path('proyectos/<int:pk>/evaluar/', views.evaluacionPTF_create, name='proyecto_evaluar'),
    #path('docente/', views.docente_list, name='docente_list'),
    #path('docente/nuevo/', views.docente_create, name='docente_create'),
    #path('docente/<int:pk>/', views.docente_detail, name='docente_detail'),
    #path('docente_delete/<int:pk>/', views.docente_delete, name='docente_delete'),
    #path('docente_edit/<int:pk>/',views.docente_edit, name='docente_edit'),
]