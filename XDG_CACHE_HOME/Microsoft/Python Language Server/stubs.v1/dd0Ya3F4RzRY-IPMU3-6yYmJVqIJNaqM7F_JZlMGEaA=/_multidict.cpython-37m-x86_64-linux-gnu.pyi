import builtins as _mod_builtins
import collections.abc as _mod_collections_abc
import multidict._abc as _mod_multidict__abc
import multidict._istr as _mod_multidict__istr

class CIMultiDict(MultiDict):
    'An ordered dictionary that can have multiple values for each key.'
    __class__ = CIMultiDict
    def __init__(self, *args, **kwargs):
        'An ordered dictionary that can have multiple values for each key.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def copy(self):
        'Return a copy of itself.'
        pass
    

class CIMultiDictProxy(MultiDictProxy):
    __class__ = CIMultiDictProxy
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _base_class = CIMultiDict()
    _proxy_classes = _mod_builtins.tuple()

Iterable = _mod_collections_abc.Iterable
class MultiDict(_Base):
    'An ordered dictionary that can have multiple values for each key.'
    __class__ = MultiDict
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __init__(self, *args, **kwargs):
        'An ordered dictionary that can have multiple values for each key.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add(self):
        'Add the key and value, not overwriting any previous value.'
        pass
    
    def clear(self):
        'Remove all items from MultiDict'
        pass
    
    def copy(self):
        'Return a copy of itself.'
        pass
    
    def extend(self):
        'Extend current MultiDict with more values.\n\n        This method must be used instead of update.\n        '
        pass
    
    def pop(self):
        'Remove the last occurrence of key and return the corresponding\n        value.\n\n        If key is not found, default is returned if given, otherwise\n        KeyError is raised.\n\n        '
        pass
    
    def popall(self):
        'Remove all occurrences of key and return the list of corresponding\n        values.\n\n        If key is not found, default is returned if given, otherwise\n        KeyError is raised.\n\n        '
        pass
    
    def popitem(self):
        'Remove and return an arbitrary (key, value) pair.'
        pass
    
    def popone(self):
        'Remove the last occurrence of key and return the corresponding\n        value.\n\n        If key is not found, default is returned if given, otherwise\n        KeyError is raised.\n\n        '
        pass
    
    def setdefault(self):
        'Return value for key, set value to default if key is not present.'
        pass
    
    def update(self):
        'Update the dictionary from *other*, overwriting existing keys.'
        pass
    

class MultiDictProxy(_Base):
    __class__ = MultiDictProxy
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _base_class = MultiDict()
    _proxy_classes = _mod_builtins.tuple()
    def copy(self):
        'Return a copy of itself.'
        pass
    

MultiMapping = _mod_multidict__abc.MultiMapping
MutableMultiMapping = _mod_multidict__abc.MutableMultiMapping
Set = _mod_collections_abc.Set
class _Base(_mod_builtins.object):
    __class__ = _Base
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _Base()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get(self):
        'Get first value matching the key.\n\n        The method is alias for .getone().\n        '
        pass
    
    def getall(self):
        'Return a list of all values matching the key.'
        pass
    
    def getone(self):
        'Get first value matching the key.'
        pass
    
    def impl(self):
        pass
    
    def items(self):
        "Return a new view of the dictionary's items *(key, value) pairs)."
        pass
    
    def keys(self):
        "Return a new view of the dictionary's keys."
        pass
    
    def values(self):
        "Return a new view of the dictionary's values."
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/yeet/.local/share/virtualenvs/NotificationScripting-FjkXIeEu/lib/python3.7/site-packages/multidict/_multidict.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'multidict._multidict'
__package__ = 'multidict'
def __pyx_unpickle__Base():
    pass

__test__ = _mod_builtins.dict()
def getversion():
    pass

istr = _mod_multidict__istr.istr
upstr = _mod_multidict__istr.istr
