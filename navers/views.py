from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from utils.decorators import assign_request_user
from utils.permissions import IsUserPermission
from .models import Naver
from .serializers import NaversListSerializer, NaversCreateSerializer, NaversDetailSerializer


class NaversViewSet(ModelViewSet):
    queryset = Naver.objects.all()
    serializer_class = NaversCreateSerializer
    permission_classes = [IsAuthenticated,IsUserPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','job_role','admission_date']
    def get_queryset(self):
        return self.request.user.navers.all()

    @assign_request_user(user_field="user")
    def create(self, request, *args, **kwargs):
        """
        Args:
            request:
            *args:
            **kwargs:
        """
        return super().create(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        self.serializer_class = NaversListSerializer
        return super().list(request, *args, **kwargs)
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = NaversDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    @assign_request_user(user_field="user")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)