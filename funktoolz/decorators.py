__all__ = ('coroutine',)


from sys import version as sys_version

from funktoolz.constants import (
    PYTHON27_VERSION,
    PYTHON34_VERSION,
    PYTHON37_VERSION,
    UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE,
)


if sys_version >= PYTHON34_VERSION and sys_version < PYTHON37_VERSION:
    from asyncio import coroutine as coroutine
elif sys_version >= PYTHON27_VERSION and sys_version < PYTHON34_VERSION:
    def coroutine(func): return func
else:
    raise Exception(UNSUPPORTED_PYTHON_VERSION_EXCEPTION_TEMPLATE % sys_version)
