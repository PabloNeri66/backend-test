from django.urls import path
from .views import InvestimentListCreateApiView

urlpatterns = [
    path(
        'api/v1/investiments/',
        InvestimentListCreateApiView.as_view(),
        name='investiment-list-create',
    ),
]
