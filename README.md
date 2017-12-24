
# Django REST framework naming style



**This is a toolkit supporting camel case and snake case APIs' naming styles and easily switch.**

I wrote this for Django 2.0 and Django REST framework 3.7.3, sorry about that I have no idea about the effects with other versions of Django or DRF.



## Requirements

* Python (3.5, 3.6)
* Django (2.0)
* Django REST framework (3.7.3)



## Installation

Install using `pip3`

```python
pip3 install django-rest-framework-naming-style
```

Replace renderer and parser classes for JSON in your `REST_FRAMEWORK` setting

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_RENDERER_CLASSES': (
        'django_rest_framework_naming_style.renderer.StylesJSONRenderer',
        # 'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'django_rest_framework_naming_style.parser.StylesJSONParser',
        # 'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    ...
}
```
Make a monkey patch in django's `manage.py`

```python
# Make patching before `execute_from_command_line(sys.argv)`
from django_rest_framework_naming_style.monkey import monkey_patch
    monkey_patch()

execute_from_command_line(sys.argv)
```



## Optional Settings

There are settings of this package with default value, options.

```python
REST_FRAMEWORK_NAMING_STYLE = {
    'STYLE_KEY': 'STYLE',  # set a header key
    'STYLE_DEFAULT': 'underscore',  # underscore/camelcase
}
```

`STYLE_KEY` that you set accept a value in request headers between `underscore` and `camelcase` to specify one naming style of APIs.

If you set `STYLE_KEY` `None`, the style only depends on `STYLE_DEFAULT` as you like.



##

Thank you for using `django-rest-framework-naming-style`.
