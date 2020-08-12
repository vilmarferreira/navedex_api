from rest_framework import serializers

class ProjectsField(serializers.RelatedField):
    def to_representation(self, value):
        return value.as_json()