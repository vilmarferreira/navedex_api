from rest_framework import permissions
from typing import Union
from navers.models import Naver
from projects.models import Project

class IsUserPermission(permissions.BasePermission):
    message = "User not allowed."

    def has_object_permission(
        self, request, view, obj: Union[Naver, Project]
    ):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Naver):
            return request.user.navers.filter(
                id=obj.id
            ).exists()

        if isinstance(obj, Project):
            return (
                request.user.projects_list.filter(
                    id=obj.id
                ).exists()
            )
