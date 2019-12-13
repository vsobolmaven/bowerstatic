# taken from pyramid.compat

from __future__ import absolute_import
import sys
import six

# True if we are running on Python 3.
PY3 = sys.version_info[0] == 3


if PY3:  # pragma: no cover
    text_type = str
else:
    text_type = six.text_type


if PY3:
    string_types = (str,)
else:
    string_types = (six.string_types,)
