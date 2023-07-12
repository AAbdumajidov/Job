from django.urls import path
from .views import CompanyListCreateAPIView, TypeListCreateAPIView, CategoryListCreateAPIView, TagListCreateAPIView, \
    CityListCreateAPIView, CountryListCreateAPIView, PositionListCreateAPIView, \
    CompanyRUDAPIView, TypeRUDAPIView, CategoryRUDAPIView, TagRUDAPIView, CityRUDAPIView, CountryRUDAPIView, PositionRUDAPIView


urlpatterns = [
    path('company/list-create/', CompanyListCreateAPIView.as_view()),
    path('company/rud/<int:pk>/', CompanyRUDAPIView.as_view()),

    path('type/list-create/', TypeListCreateAPIView.as_view()),
    path('type/rud/<int:pk>/', TypeRUDAPIView.as_view()),

    path('cat/list-create/', CategoryListCreateAPIView.as_view()),
    path('cat/rud/<int:pk>/', CategoryRUDAPIView.as_view()),

    path('tag/list-create/', TagListCreateAPIView.as_view()),
    path('tag/rud/<int:pk>/', TagRUDAPIView.as_view()),

    path('city/list-create/', CityListCreateAPIView.as_view()),
    path('city/rud/<int:pk>/', CityRUDAPIView.as_view()),

    path('country/list-create/', CountryListCreateAPIView.as_view()),
    path('country/rud/<int:pk>/', CountryRUDAPIView.as_view()),

    path('position/list-create/', PositionListCreateAPIView.as_view()),
    path('position/rud/<int:pk>/', PositionRUDAPIView.as_view()),
]
