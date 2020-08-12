from rest_framework import serializers

from navers.RelatedFieldSerializer import ProjectsField
from navers.models import Naver
from projects.models import Project


class NaversCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        fields = '__all__'
class NaversListSerializer(serializers.ModelSerializer):
    job_role = serializers.SerializerMethodField()

    class Meta:
        model = Naver
        exclude=['user']

    def get_job_role(self, obj):
        return obj.get_job_role_display()
class NaversDetailSerializer(NaversListSerializer):
    projects = ProjectsField(many=True,read_only=True)


