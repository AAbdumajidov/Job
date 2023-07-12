from django.urls import path
from .views import AccountListAPIView, AccountRUDAPIView, WorkHistoryListCreateAPIView, WorkHistoryRUDAPIView


urlpatterns = [
    path('list/', AccountListAPIView.as_view()),
    path('detail/<int:pk>/', AccountRUDAPIView.as_view()),

    path('work/list/', WorkHistoryListCreateAPIView.as_view()),
    path('work/rud/<int:pk>/', WorkHistoryRUDAPIView.as_view()),
]