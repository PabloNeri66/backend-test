from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Investiment
from .serializers import (
    InvestimentListSerializer,
    InvestimentCreateSerializer,
    InvestimentWithdrawnSerializer,
)


class InvestimentListCreateApiView(ListCreateAPIView):
    queryset = Investiment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InvestimentListSerializer
        return InvestimentCreateSerializer


class InvestimentRetrieveApiView(RetrieveAPIView):
    queryset = Investiment.objects.all()
    serializer_class = InvestimentListSerializer


class InvestimentWithdrawnUpdateApiView(UpdateAPIView):
    queryset = Investiment.objects.all()
    serializer_class = InvestimentWithdrawnSerializer
