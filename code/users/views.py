from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView

from .serializers import UserCreateSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
