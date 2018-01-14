"""
Make something in django rest framework patch.
"""
from __future__ import unicode_literals

from .parser import StylesQueryParamsParser


def monkey_patch():
    """
    Make sure this function be executed early enough.
    Suggest before `execute_from_command_line(sys.argv)` in `manage.py`.
    """
    patch_django_rest_framework_request()


def patch_django_rest_framework_request():
    from django.utils.functional import cached_property
    from rest_framework.request import Request

    def query_params(self):
        return StylesQueryParamsParser.parse(self._request.GET, self)

    setattr(Request, 'query_params', cached_property(query_params))
