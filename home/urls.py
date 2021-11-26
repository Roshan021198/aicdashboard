from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('query_message/', views.query_message,name='query_message'),
    path('SWEA/', views.SWEA,name='SWEA'),
    path('callForApplications/', views.callForApplication,name='callForApplication'),
    path('apply_cohort_2/', views.CFA,name='CFA'),

    path('test123/',views.test123,name='test123'),
]
