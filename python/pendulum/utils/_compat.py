from __future__ import annotations

import sys

from pendulum.utils import _zoneinfo as zoneinfo


PYPY = hasattr(sys, "pypy_version_info")

from importlib import resources


__all__ = ["resources", "zoneinfo"]
