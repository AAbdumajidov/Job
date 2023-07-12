from rest_framework import generics
from .serializers import JobListSerializer, JobUpdateSerializer
from .models import Job


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer


class JobRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
