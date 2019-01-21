from collections import OrderedDict
from threading import RLock
import sys
import time

class ExpiringDict(OrderedDict):
        def __init__(self, cache_len, max_age):
            assert cache_len >= 1
            assert max_age >= 0

            OrderedDict.__init__(self)
            self.cache_len = cache_len
            self.max_age = max_age
            self.lock = RLock()

            self._safe_keys = lambda: list(self.keys())

        # method which returns true if dictionary has the key
        def __contains__(self, key):
            try:
                with self.lock:
                    item = OrderedDict.__getitem__(self, key)
                    if time.time() - item[1] < self.max_age:
                        return True
                    else:
                        del self[key]
            except KeyError:
                pass
            return False

        # method which returns the item of the dictionary
        def __getitem__(self, key, with_age=False):
            with self.lock:
                item = OrderedDict.__getitem__(self, key)
                item_age = time.time() - item[1]
                if item_age < self.max_age:
                    if with_age:
                        return item[0], item_age
                    else:
                        return item[0]
                else:
                    del self[key]
                    raise KeyError(key)

        # method which assigns value to key
        def __setitem__(self, key, value):
            with self.lock:
                if len(self) == self.cache_len:
                    try:
                        self.popitem(last=False)
                    except KeyError:
                        pass
                OrderedDict.__setitem__(self, key, (value, time.time()))

        # method which gets the value at the key and deletes the values
        # returns None if the value has expired
        def pop(self, key):
            with self.lock:
                try:
                    item = OrderedDict.__getitem__(self, key)
                    del self[key]
                    return item[0]
                except KeyError:
                    return None

        # method which returns the time to life of a value
        # returns None if key doesnt exist or expired
        def ttl(self, key):
            key_value, key_age = self.get(key, with_age=True)
            if key_age:
                key_ttl = self.max_age - key_age
                if key_ttl > 0:
                    return key_ttl
            return None

        # method which returns value at a specified key
        def get(self, key, with_age=False):
            try:
                return self.__getitem__(key, with_age)
            except KeyError:
                if with_age:
                    return None, None
                else:
                    return None

        # method which returns a list of the dict's keys and values
        def items(self):
            r = []
            for key in self._safe_keys():
                try:
                    r.append((key, self[key]))
                except KeyError:
                    pass
            return r

        # method which returns a list of the dict's values
        def values(self):
            r = []
            for key in self._safe_keys():
                try:
                    r.append(self[key])
                except KeyError:
                    pass
            return r
