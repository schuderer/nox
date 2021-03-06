__all__ = ["TYPE_CHECKING", "NoReturn", "Python"]

import typing as _typing

try:
    from typing import TYPE_CHECKING
except ImportError:
    try:
        from typing_extensions import TYPE_CHECKING
    except ImportError:
        TYPE_CHECKING = False

try:
    from typing import NoReturn
except ImportError:
    try:
        from typing_extensions import NoReturn
    except ImportError:
        pass

Python = _typing.Optional[_typing.Union[str, _typing.Sequence[str], bool]]
