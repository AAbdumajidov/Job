from django.urls import path
from .views import JobListCreateAPIView, JobRUDAPIView


urlpatterns = [
    path('list/', JobListCreateAPIView.as_view()),
    path('rud/<int:pk>/', JobRUDAPIView.as_view())
]