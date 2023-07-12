from rest_framework import generics
from .serializers import AccountSerializer, WorkHistorySerializer
from .models import Account, WorkHistory


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if qs:
            return qs.filter(type=1)
        return qs


class AccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class WorkHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer


class WorkHistoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer


