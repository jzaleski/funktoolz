__all__ = ('From',)


from sys import version as sys_version

from funktoolz.constants import (
    EMPTY_STRING,
    PYTHON27_VERSION,
    PYTHON34_VERSION,
    PYTHON35_VERSION,
    PYTHON37_VERSION,
    UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE,
)


ASYNC = 'async '
AWAIT = 'await '
COROUTINE_DECORATOR = '@coroutine'
COROUTINE_IMPORT = \
    'from %s.decorators import coroutine' % __name__.split('.')[0]
FROM_METHOD_TEMPLATE = """
%s

%s
%sdef From(
    func,
    *args,
    **kwargs
):
    return %sfunc(*args, **kwargs)
"""
YIELD_FROM = 'yield from '


def _get_from_method_definition(sys_version):
    return (FROM_METHOD_TEMPLATE % \
        _get_from_method_template_args(sys_version)).strip()


def _get_from_method_template_args(sys_version):
    if sys_version >= PYTHON35_VERSION and sys_version < PYTHON37_VERSION:
        return (
            EMPTY_STRING,
            EMPTY_STRING,
            ASYNC,
            AWAIT,
        )
    elif sys_version >= PYTHON34_VERSION and sys_version < PYTHON35_VERSION:
        return (
            COROUTINE_IMPORT,
            COROUTINE_DECORATOR,
            EMPTY_STRING,
            YIELD_FROM,
        )
    elif sys_version >= PYTHON27_VERSION and sys_version < PYTHON34_VERSION:
        return (
            EMPTY_STRING,
            EMPTY_STRING,
            EMPTY_STRING,
            EMPTY_STRING,
        )
    raise Exception(UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE % sys_version)


exec(_get_from_method_definition(sys_version))
