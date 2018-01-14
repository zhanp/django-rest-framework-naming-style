from __future__ import unicode_literals

import re


def to_camel_case(value):
    return re.compile(r'(_+[a-z])').sub(
        lambda m: m.group().upper().lstrip('_'), value)


def to_snake_case(value):
    return re.compile(r'([A-Z])').sub(
        lambda m: '_%s' % m.group().lower(), value)


def foo(data, func):
    if isinstance(data, dict):
        return {func(k): foo(v, func) for k, v in data.items()}
    if isinstance(data, (list, tuple)):
        return [foo(item, func) for item in data]
    return data


def camel_case_foo(data):
    return foo(data, to_camel_case)


def snake_case_foo(data):
    return foo(data, to_snake_case)
