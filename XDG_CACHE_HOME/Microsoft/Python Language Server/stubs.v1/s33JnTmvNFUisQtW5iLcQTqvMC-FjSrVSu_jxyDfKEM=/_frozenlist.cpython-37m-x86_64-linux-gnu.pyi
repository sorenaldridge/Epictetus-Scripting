import builtins as _mod_builtins
import collections.abc as _mod_collections_abc

class FrozenList(_mod_builtins.object):
    __class__ = FrozenList
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
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
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return FrozenList()
    
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
    
    def __reversed__(self):
        pass
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self):
        pass
    
    def clear(self):
        pass
    
    def count(self):
        pass
    
    def extend(self):
        pass
    
    def freeze(self):
        pass
    
    @property
    def frozen(self):
        pass
    
    def index(self):
        pass
    
    def insert(self):
        pass
    
    def pop(self):
        pass
    
    def remove(self):
        pass
    
    def reverse(self):
        pass
    

MutableSequence = _mod_collections_abc.MutableSequence
__builtins__ = {}
__doc__ = None
__file__ = '/home/yeet/.local/share/virtualenvs/NotificationScripting-FjkXIeEu/lib/python3.7/site-packages/aiohttp/_frozenlist.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'aiohttp._frozenlist'
__package__ = 'aiohttp'
def __pyx_unpickle_FrozenList():
    pass

__test__ = _mod_builtins.dict()
