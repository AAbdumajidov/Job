from django.urls import path
from .views import ContactListCreateAPIView, SubscribeListCreateAPIView

urlpatterns = [
    path('contact/list-create', ContactListCreateAPIView.as_view()),
    path('subscribe/list-create', SubscribeListCreateAPIView.as_view())
]