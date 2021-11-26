from django.urls import path
from . import views

urlpatterns = [
    path('', views.ideanest,name='ideanest'),
    path('ideanest_form', views.ideanest_form,name='ideanest_form_iframe'),

    path('ideanest_nomination', views.ideanest_nomination,name='ideanest_nomination'),
    path('ideanest_dashboard', views.ideanest_dashboard,name='ideanest_dashboard'),
    path('create_ideanest_session', views.create_ideanest_session,name='create_ideanest_session'),
    path('ideanest_submission', views.ideanest_submission,name='ideanest_submission'),
    path('ideanest_edit_form/<int:pk>/edit_ideanest/', views.ideanest_edit_form,name='ideanest_edit_form'),
    path('ideanest_excel/', views.ideanest_excel,name='ideanest_excel'),
    path('ideanest_recording/', views.ideanest_recording,name='ideanest_recording'),
]
