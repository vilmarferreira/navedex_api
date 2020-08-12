from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from projects.models import Project
from navers.serializers import NaversListSerializer

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    def validate(self, attrs):
        listError = []
        for naver in attrs['navers']:
            if naver.user != attrs['user']:
                listError.append(naver.id)
        if listError.__len__() > 0 :
            raise ValidationError({'error': {'Naver does not exist at its base': listError,

                                             }}
                                  )

        return attrs
class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = [
            'user',
            'navers'
        ]
class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = [
            'user'
        ]
    def to_representation(self, instance):
        self.fields['navers'] = NaversListSerializer( read_only=True, many=True)
        return super().to_representation(instance)