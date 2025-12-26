from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Investor
from .serializers import InvestorSerializer


class InvestorListCreateApiView(ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class InvestorRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
