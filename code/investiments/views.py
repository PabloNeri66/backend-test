from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Investiment
from . serializers import (
    InvestimentListSerializer,
    InvestimentCreateSerializer,
)


class InvestimentListCreateApiView(ListCreateAPIView):
    queryset = Investiment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InvestimentListSerializer
        return InvestimentCreateSerializer


class InvestimentRetrieveApiView(RetrieveAPIView):
    pass


class InvestimentWithdrawnUpdateApiView(UpdateAPIView):
    pass
