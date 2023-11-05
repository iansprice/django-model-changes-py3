import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-model-changes-py3',
    version='0.15.2',
    packages=find_packages(exclude=['tests']),
    license='MIT License',
    description='django-model-changes allows you to track model instance changes.',
    long_description=README,
    url='http://github.com/iansprice/django-model-changes-py3',
    author='Ian Price',
    author_email='iprice@thermaline.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='runtests.runtests',
    tests_require=[
        'django<2.1'
    ],
    zip_safe=True,
)
