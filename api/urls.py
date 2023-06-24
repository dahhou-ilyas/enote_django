from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes,name="routes"),
    path('notes/',views.getNotes,name="notes"),
    path('notes/<str:pk>/update/',views.updateNote,name="updateNote"),
    path('notes/<str:pk>/delete/',views.deleteNote,name="deleteNote"),
    
    path('notes/<str:pk>/',views.getNote,name="note"),
]
