__all__ = (
    'Filter',
    'From',
    'Lambda',
    'Map',
    'Reduce',
)


from sys import version as sys_version

from funktoolz.constants import (
    EMPTY_STRING,
    PYTHON27_VERSION,
    PYTHON28_VERSION,
    PYTHON34_VERSION,
    PYTHON35_VERSION,
    PYTHON37_VERSION,
    UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE,
)


ASYNC = 'async '
COROUTINE_DECORATOR = '@coroutine'
COROUTINE_IMPORT = 'from %s.decorators import coroutine' % \
    __name__.split('.')[0]
FILTER_FUNCTION_TEMPLATE = """
%s
%sdef Filter(function, iterable):
    return filter(function, iterable)
"""
FROM_FUNCTION_TEMPLATE = """
%s
%sdef From(
    function,
    *args,
    **kwargs
):
    warn('Method `From` is deprecated, use `Lambda`')
    return function(*args, **kwargs)
"""
LAMBDA_FUNCTION_TEMPLATE = """
%s
%sdef Lambda(
    function,
    *args,
    **kwargs
):
    return function(*args, **kwargs)
"""
MAP_FUNCTION_TEMPLATE = """
%s
%sdef Map(function, iterable):
    return map(function, iterable)
"""
REDUCE_IMPORT = 'from functools import reduce'
REDUCE_FUNCTION_TEMPLATE = """
%s
%sdef Reduce(
    function,
    iterable,
    initializer=None
):
    return reduce(
        function,
        iterable,
        initializer
    )
"""
WARN_IMPORT = 'from warnings import warn'


def _get_filter_function_definition(sys_version):
    return (FILTER_FUNCTION_TEMPLATE % \
        _get_function_template_args(sys_version)).strip()


def _get_from_function_definition(sys_version):
    return (FROM_FUNCTION_TEMPLATE % \
        _get_function_template_args(sys_version)).strip()


def _get_from_import_definition(sys_version):
    return '\n\n'.join(
        '\n'.join(function(sys_version))
        for function in (_get_system_from_import_args,
            _get_module_from_import_args)
    ).strip()


def _get_function_template_args(sys_version):
    if sys_version >= PYTHON35_VERSION and sys_version < PYTHON37_VERSION:
        return (EMPTY_STRING, ASYNC)
    elif sys_version >= PYTHON34_VERSION and sys_version < PYTHON35_VERSION:
        return (COROUTINE_DECORATOR, EMPTY_STRING)
    elif sys_version >= PYTHON27_VERSION and sys_version < PYTHON28_VERSION:
        return (EMPTY_STRING, EMPTY_STRING)
    raise Exception(UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE % sys_version)


def _get_lambda_function_definition(sys_version):
    return (LAMBDA_FUNCTION_TEMPLATE % \
        _get_function_template_args(sys_version)).strip()


def _get_map_function_definition(sys_version):
    return (MAP_FUNCTION_TEMPLATE % \
        _get_function_template_args(sys_version)).strip()


def _get_module_definition(sys_version):
    return '\n\n\n'.join(
        function(sys_version)
        for function in (
            _get_from_import_definition,
            _get_filter_function_definition,
            _get_from_function_definition,
            _get_lambda_function_definition,
            _get_map_function_definition,
            _get_reduce_function_definition,
        )
    ).strip()


def _get_module_from_import_args(sys_version):
    if sys_version >= PYTHON35_VERSION and sys_version < PYTHON37_VERSION:
        return tuple()
    elif sys_version >= PYTHON34_VERSION and sys_version < PYTHON35_VERSION:
        return (COROUTINE_IMPORT,)
    elif sys_version >= PYTHON27_VERSION and sys_version < PYTHON28_VERSION:
        return tuple()
    raise Exception(UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE % sys_version)


def _get_reduce_function_definition(sys_version):
    return (REDUCE_FUNCTION_TEMPLATE % \
        _get_function_template_args(sys_version)).strip()


def _get_system_from_import_args(sys_version):
    if sys_version >= PYTHON35_VERSION and sys_version < PYTHON37_VERSION:
        return (REDUCE_IMPORT, WARN_IMPORT)
    elif sys_version >= PYTHON34_VERSION and sys_version < PYTHON35_VERSION:
        return (REDUCE_IMPORT, WARN_IMPORT)
    elif sys_version >= PYTHON27_VERSION and sys_version < PYTHON28_VERSION:
        return (WARN_IMPORT,)
    raise Exception(UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE % sys_version)


exec(_get_module_definition(sys_version))
