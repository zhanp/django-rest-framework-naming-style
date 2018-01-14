from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer

from .naming import camel_case_foo
from .utils import get_style


class StylesJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if get_style(renderer_context['request']) == 'camelcase':
            data = camel_case_foo(data)
        return super(StylesJSONRenderer, self).render(
            data, accepted_media_type, renderer_context)
