from django.urls import path
from .views.status_graph import status_grpah

urlpatterns = [
    path("template/<int:template_id>/status_graph.png", status_grpah)
]