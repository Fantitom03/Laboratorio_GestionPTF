from django.urls import path
from . import views

app_name = 'persona'

urlpatterns = [
    #persona views
    path('docente/', views.docente_list, name='docente_list'),
    path('docente/nuevo/', views.docente_create, name='docente_create'),
    path('<int:pk>/',views.docente_detail, name='docente_detail'),

]

