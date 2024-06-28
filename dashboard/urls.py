from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.dashboard, name = 'dashboard'),
    # path('',views.admin_dashboard, name = 'dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('wakil_kesiswaan_dashboard/', views.wakil_kesiswaan_dashboard, name='wakil_kesiswaan_dashboard'),
]