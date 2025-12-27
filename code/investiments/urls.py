from django.urls import path
from .views import (
    InvestimentListCreateApiView,
    InvestimentRetrieveApiView,
    InvestimentWithdrawnUpdateApiView,
)

urlpatterns = [
    path(
        'api/v1/investiments/',
        InvestimentListCreateApiView.as_view(),
        name='investiment-list-create',
    ),
    path(
        'api/v1/investiments/<uuid:pk>/',
        InvestimentRetrieveApiView.as_view(),
        name='investiment-detail-update-delete',
    ),
    path(
        'api/v1/investiments/<uuid:pk>/withdrawn/',
        InvestimentWithdrawnUpdateApiView.as_view(),
        name='investiment-withdrawn-update',
    ),
]
