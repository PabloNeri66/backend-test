from django.urls import path
from .views import (
    InvestorListCreateApiView,
    InvestorRetrieveUpdateDestroyApiView,
)

urlpatterns = [
    path(
        'api/v1/investors/',
        InvestorListCreateApiView.as_view(),
        name='investor-list-create',
    ),
    path(
        'api/v1/investors/<int:pk>/',
        InvestorRetrieveUpdateDestroyApiView.as_view(),
        name='investor-detail-update-delete'
    ),
]
