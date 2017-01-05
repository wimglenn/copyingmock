from copy import deepcopy

try:
    # Python 3.3+
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock


class CopyingMock(MagicMock):

    def __call__(self, *args, **kwargs):
        args = deepcopy(args)
        kwargs = deepcopy(kwargs)
        return super(CopyingMock, self).__call__(*args, **kwargs)
