from __future__ import unicode_literals

from django.conf import settings
from rest_framework.settings import api_settings


try:
    setting = settings.REST_FRAMEWORK_NAMING_STYLE
except AttributeError:
    setting = {}

STYLE_KEY = setting.get('STYLE_KEY', 'STYLE')
HEADER_KEY = 'HTTP_%s' % STYLE_KEY.upper() if STYLE_KEY else None
STYLE_DEFAULT = setting.get('STYLE_DEFAULT', 'underscore')
ORDERING_PARAM = api_settings.ORDERING_PARAM


def get_style(request):
    try:
        style = request.parser_context['view'].style
    except (AttributeError, KeyError):
        style = request.META.get(HEADER_KEY) if HEADER_KEY else None

    if style in ('underscore', 'camelcase'):
        return style
    return STYLE_DEFAULT
