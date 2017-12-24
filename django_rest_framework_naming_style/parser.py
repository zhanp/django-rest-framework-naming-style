from django.http import QueryDict
from rest_framework.parsers import JSONParser

from .naming import to_snake_case, snake_case_foo
from .utils import get_style, ORDERING_PARAM


class StylesJSONParser(JSONParser):
    def parse(self, stream, *args, **kwargs):
        data = super(StylesJSONParser, self).parse(stream, *args, **kwargs)
        return snake_case_foo(data) if get_style(stream) == 'camelcase' else data


class StylesQueryParamsParser(object):
    """
    For formatting request query params, not a rest framework parser class.
    """
    @staticmethod
    def parse(query_params, request):
        if get_style(request) == 'camelcase':
            q = QueryDict('', mutable=True, encoding=query_params.encoding)
            for k, l in query_params.lists():
                q.setlist(
                    to_snake_case(k),
                    k != ORDERING_PARAM and l or list(map(to_snake_case, l)))
            q._mutable = False
            return q

        else:
            return query_params
