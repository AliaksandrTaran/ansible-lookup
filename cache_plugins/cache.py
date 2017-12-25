from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import codecs

try:
    import simplejson as json
except ImportError:
    import json

from ansible.parsing.utils.jsonify import jsonify
from ansible.plugins.cache import BaseFileCacheModule


class CacheModule(BaseFileCacheModule):

    def _load(self, filepath):
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _dump(self, value, filepath):
        with codecs.open(filepath, 'w', encoding='utf-8') as f:
	f.write(jsonify(value, format=True))
