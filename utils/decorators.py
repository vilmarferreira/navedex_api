"""decorators
"""

from typing import Callable

from django.http import QueryDict
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotAuthenticated, APIException


def assign_request_user(user_field: str = 'user'):
    """insere o usuário da sessão nos dados enviados pela requisição

    Keyword Arguments:
        user_field {str} -- campo do usuário (default: {'user'})

    Raises:
        NotAuthenticated: Não autenticado
        APIException: Erro

    Returns:
        Callable -- função
    """

    def decorator(func: Callable):
        def new_func(self, request, *args, **kwargs):
            if not request.user or not request.user.pk:
                raise NotAuthenticated(_("Not authenticated"))
            if isinstance(request.data, QueryDict):
                request.data._mutable = True  # pylint: disable=protected-access
            try:
                # request.data._mutable = True
                request.data[user_field] = request.user.pk
            except AttributeError as err:
                raise NotAuthenticated(_("Not authenticated - " + str(err)))
            except Exception as err:
                raise APIException(str(err))
            return func(self, request, *args, **kwargs)
        return new_func

    return decorator
