from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects.models import Project
from projects.serializers import ProjectListSerializer, ProjectCreateSerializer, ProjectDetailSerializer
from utils.decorators import assign_request_user
from utils.permissions import IsUserPermission


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated, IsUserPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ProjectDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.projects_list.all()

    @assign_request_user(user_field="user")
    def create(self, request, *args, **kwargs):
        """
        Args:
            request:
            *args:
            **kwargs:
        """
        return super().create(request, *args, **kwargs)

    @assign_request_user(user_field="user")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        self.serializer_class = ProjectListSerializer
        return super().list(request, *args, **kwargs)

