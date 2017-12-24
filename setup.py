# noinspection PyPackageRequirements
from pypandoc import convert_file
from setuptools import setup, find_packages

version = __import__('django_rest_framework_naming_style').__version__

long_description = convert_file('README.md', 'rst')

setup(
    name='django-rest-framework-naming-style',
    version=version,
    url='https://github.com/zhanp/django-rest-framework-naming-style',
    author='Fitz ZP',
    author_email='zhanp.cn@gmail.com',
    description='A toolkit for Django REST framework '
                'to easily switch APIs\' naming styles.',
    long_description=long_description,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django :: 2.0',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
