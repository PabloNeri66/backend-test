from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Investiment


class InvestimentListCreateApiView(ListCreateAPIView):
    queryset = Investiment.objects.all().only(
        'id',
        'created_at',
        'investor',
        'value',
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return None
        return None


class InvestimentRetrieveApiView(RetrieveAPIView):
    pass


class InvestimentWithdrawnUpdateApiView(UpdateAPIView):
    pass
