import aiohttp.http_exceptions as _mod_aiohttp_http_exceptions
import aiohttp.http_parser as _mod_aiohttp_http_parser
import aiohttp.http_writer as _mod_aiohttp_http_writer
import aiohttp.streams as _mod_aiohttp_streams
import builtins as _mod_builtins
import multidict._multidict as _mod_multidict__multidict
import yarl as _mod_yarl

BadHttpMessage = _mod_aiohttp_http_exceptions.BadHttpMessage
BadStatusLine = _mod_aiohttp_http_exceptions.BadStatusLine
ContentLengthError = _mod_aiohttp_http_exceptions.ContentLengthError
class HttpRequestParser(HttpParser):
    __class__ = HttpRequestParser
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class HttpResponseParser(HttpParser):
    __class__ = HttpResponseParser
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

InvalidHeader = _mod_aiohttp_http_exceptions.InvalidHeader
InvalidURLError = _mod_aiohttp_http_exceptions.InvalidURLError
LineTooLong = _mod_aiohttp_http_exceptions.LineTooLong
PayloadEncodingError = _mod_aiohttp_http_exceptions.PayloadEncodingError
class RawRequestMessage(_mod_builtins.object):
    __class__ = RawRequestMessage
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
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
    
    def _replace(self):
        pass
    
    @property
    def chunked(self):
        pass
    
    @property
    def compression(self):
        pass
    
    @property
    def headers(self):
        pass
    
    @property
    def method(self):
        pass
    
    @property
    def path(self):
        pass
    
    @property
    def raw_headers(self):
        pass
    
    @property
    def should_close(self):
        pass
    
    @property
    def upgrade(self):
        pass
    
    @property
    def url(self):
        pass
    
    @property
    def version(self):
        pass
    

class RawResponseMessage(_mod_builtins.object):
    __class__ = RawResponseMessage
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
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
    
    @property
    def chunked(self):
        pass
    
    @property
    def code(self):
        pass
    
    @property
    def compression(self):
        pass
    
    @property
    def headers(self):
        pass
    
    @property
    def raw_headers(self):
        pass
    
    @property
    def reason(self):
        pass
    
    @property
    def should_close(self):
        pass
    
    @property
    def upgrade(self):
        pass
    
    @property
    def version(self):
        pass
    

TransferEncodingError = _mod_aiohttp_http_exceptions.TransferEncodingError
_CIMultiDict = _mod_multidict__multidict.CIMultiDict
_CIMultiDictProxy = _mod_multidict__multidict.CIMultiDictProxy
_DeflateBuffer = _mod_aiohttp_http_parser.DeflateBuffer
_EMPTY_PAYLOAD = _mod_aiohttp_streams.EmptyStreamReader()
_HttpVersion = _mod_aiohttp_http_writer.HttpVersion
_HttpVersion10 = _mod_aiohttp_http_writer.HttpVersion()
_HttpVersion11 = _mod_aiohttp_http_writer.HttpVersion()
_StreamReader = _mod_aiohttp_streams.StreamReader
_URL = _mod_yarl.URL
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = None
__file__ = '/home/yeet/.local/share/virtualenvs/NotificationScripting-FjkXIeEu/lib/python3.7/site-packages/aiohttp/_http_parser.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'aiohttp._http_parser'
__package__ = 'aiohttp'
def __pyx_unpickle_RawRequestMessage():
    pass

def __pyx_unpickle_RawResponseMessage():
    pass

__test__ = _mod_builtins.dict()
i = 33
def parse_url():
    pass

