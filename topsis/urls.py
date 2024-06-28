from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("input/", views.input, name="input"),
    path("analyze/", views.analysis, name="analyze"),
    path("analyze_wakil/", views.analysis_wakil, name="analyze_wakil"),
    path("analyze/<int:year>/", views.analysis, name="analyze_year"),  # Ubah path untuk menerima parameter tahun
    path("analyze_wakil/", views.analysis_wakil, name="analyze_wakil"),
    path("<int:year>/", views.index, name="index_year"),  # Add a path for handling the year parameter
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='topsis.update'),
    path('delete/<int:id>',views.delete, name='topsis.delete'),
]
