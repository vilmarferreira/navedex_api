from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

from users.serializers import RegisterSerializer

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class RegisterView(JSONWebTokenAPIView):
    """View para registro"""
    serializer_class = RegisterSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """
        Args:
            request:
            *args:
            **kwargs:
        """
        sid = transaction.savepoint()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data,status.HTTP_201_CREATED)
            transaction.savepoint_commit(sid)
            return response
        transaction.savepoint_rollback(sid)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)