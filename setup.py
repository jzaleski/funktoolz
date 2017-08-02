import ast, re

from setuptools import find_packages, setup


MODULE_NAME = 'funktoolz'


_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('{}/__init__.py'.format(MODULE_NAME), 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name=MODULE_NAME,
    version=version,
    description='Gap bridging function[al] backports for PY2/PY3 compatibility',
    author='Jonathan W. Zaleski',
    author_email='JonathanZaleski@gmail.com',
    url='https://github.com/jzaleski/{}'.format(MODULE_NAME),
    packages=find_packages(exclude=('tests', 'tests.*')),
    install_requires=['setuptools'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='pytest',
    include_package_data=True,
)
