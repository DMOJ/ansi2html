from __future__ import annotations

from ansi2html.converter import Ansi2HTMLConverter

try:
    # pyright: reportMissingImport=false
    from ansi2html._version import __version__  # mypy: disable
except ImportError:  # pragma: no branch
    try:
        from importlib.metadata import version
    except ImportError:
        from importlib_metadata import version
    __version__ = version("ansi2html")

__all__ = ("Ansi2HTMLConverter", "__version__")
