from django.urls import path
from . import views

urlpatterns = [
    path('', views.sanvriddhi,name='sanvriddhi'),
    path('sanvriddhi_form', views.sanvriddhi_form,name='iframe'),
    path('sanvriddhi_nomination', views.sanvriddhi_nomination,name='sanvriddhi_nomination'),
    path('sanvriddhi_dashboard', views.sanvriddhi_dashboard,name='sanvriddhi_dashboard'),
    path('create_session', views.create_session,name='create_session'),
    path('submission', views.submission,name='submission'),
    path('sanvriddhi_edit_form/<int:pk>/edit_sanvriddhi/', views.sanvriddhi_edit_form,name='sanvriddhi_edit_form'),
    path('sanvriddhi_excel/', views.sanvriddhi_excel,name='sanvriddhi_excel'),
    path('sanvriddhi_recording/', views.sanvriddhi_recording,name='sanvriddhi_recording'),



]
