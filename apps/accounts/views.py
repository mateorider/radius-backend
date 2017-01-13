from rest_framework import status, views, viewsets, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.base_accounts.views import BaseUserViewSet


class UserViewSet(BaseUserViewSet):
    pass
