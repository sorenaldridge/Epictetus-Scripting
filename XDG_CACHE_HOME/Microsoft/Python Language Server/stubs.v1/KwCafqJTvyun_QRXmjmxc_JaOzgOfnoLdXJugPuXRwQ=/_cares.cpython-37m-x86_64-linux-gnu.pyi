import builtins as _mod_builtins

__doc__ = None
__file__ = '/home/yeet/.local/share/virtualenvs/NotificationScripting-FjkXIeEu/lib/python3.7/site-packages/pycares/_cares.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'pycares._cares'
__package__ = 'pycares'
ffi = _mod_builtins.CompiledFFI()
class lib(_mod_builtins.object):
    ARES_AI_ADDRCONFIG = 64
    ARES_AI_ALL = 32
    ARES_AI_CANONIDN = 8192
    ARES_AI_CANONNAME = 1
    ARES_AI_IDN = 1024
    ARES_AI_IDN_ALLOW_UNASSIGNED = 2048
    ARES_AI_IDN_USE_STD3_ASCII_RULES = 4096
    ARES_AI_MASK = 127
    ARES_AI_NUMERICHOST = 2
    ARES_AI_NUMERICSERV = 8
    ARES_AI_PASSIVE = 4
    ARES_AI_V4MAPPED = 16
    ARES_EADDRGETNETWORKPARAMS = 23
    ARES_EBADFAMILY = 9
    ARES_EBADFLAGS = 18
    ARES_EBADHINTS = 20
    ARES_EBADNAME = 8
    ARES_EBADQUERY = 7
    ARES_EBADRESP = 10
    ARES_EBADSTR = 17
    ARES_ECANCELLED = 24
    ARES_ECONNREFUSED = 11
    ARES_EDESTRUCTION = 16
    ARES_EFILE = 14
    ARES_EFORMERR = 2
    ARES_ELOADIPHLPAPI = 22
    ARES_ENODATA = 1
    ARES_ENOMEM = 15
    ARES_ENONAME = 19
    ARES_ENOTFOUND = 4
    ARES_ENOTIMP = 5
    ARES_ENOTINITIALIZED = 21
    ARES_EOF = 13
    ARES_EREFUSED = 6
    ARES_ESERVFAIL = 3
    ARES_ETIMEOUT = 12
    ARES_FLAG_EDNS = 256
    ARES_FLAG_IGNTC = 4
    ARES_FLAG_NOALIASES = 64
    ARES_FLAG_NOCHECKRESP = 128
    ARES_FLAG_NORECURSE = 8
    ARES_FLAG_NOSEARCH = 32
    ARES_FLAG_PRIMARY = 2
    ARES_FLAG_STAYOPEN = 16
    ARES_FLAG_USEVC = 1
    ARES_GETSOCK_MAXNUM = 16
    @staticmethod
    def ARES_GETSOCK_READABLE():
        'int ARES_GETSOCK_READABLE(int, int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ARES_GETSOCK_WRITABLE():
        'int ARES_GETSOCK_WRITABLE(int, int);\n\nCFFI C function from _cares.lib'
        pass
    
    ARES_LIB_INIT_ALL = 1
    ARES_NI_DCCP = 64
    ARES_NI_DGRAM = 16
    ARES_NI_IDN = 1024
    ARES_NI_IDN_ALLOW_UNASSIGNED = 2048
    ARES_NI_IDN_USE_STD3_ASCII_RULES = 4096
    ARES_NI_LOOKUPHOST = 256
    ARES_NI_LOOKUPSERVICE = 512
    ARES_NI_NAMEREQD = 4
    ARES_NI_NOFQDN = 1
    ARES_NI_NUMERICHOST = 2
    ARES_NI_NUMERICSCOPE = 128
    ARES_NI_NUMERICSERV = 8
    ARES_NI_SCTP = 32
    ARES_NI_TCP = 0
    ARES_NI_UDP = 16
    ARES_OPT_DOMAINS = 128
    ARES_OPT_EDNSPSZ = 32768
    ARES_OPT_FLAGS = 1
    ARES_OPT_LOOKUPS = 256
    ARES_OPT_NDOTS = 8
    ARES_OPT_RESOLVCONF = 131072
    ARES_OPT_ROTATE = 16384
    ARES_OPT_SERVERS = 64
    ARES_OPT_SOCK_RCVBUF = 4096
    ARES_OPT_SOCK_SNDBUF = 2048
    ARES_OPT_SOCK_STATE_CB = 512
    ARES_OPT_SORTLIST = 1024
    ARES_OPT_TCP_PORT = 32
    ARES_OPT_TIMEOUT = 2
    ARES_OPT_TIMEOUTMS = 8192
    ARES_OPT_TRIES = 4
    ARES_OPT_UDP_PORT = 16
    ARES_SOCKET_BAD = -1
    ARES_SUCCESS = 0
    C_IN = 1
    INET6_ADDRSTRLEN = 46
    INET_ADDRSTRLEN = 16
    T_A = 1
    T_AAAA = 28
    T_ANY = 255
    T_CNAME = 5
    T_MX = 15
    T_NAPTR = 35
    T_NS = 2
    T_PTR = 12
    T_SOA = 6
    T_SRV = 33
    T_TXT = 16
    @staticmethod
    def ares_cancel():
        'void ares_cancel(struct ares_channeldata *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_create_query():
        'int ares_create_query(char *, int, int, unsigned short, int, unsigned char * *, int *, int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_destroy():
        'void ares_destroy(struct ares_channeldata *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_destroy_options():
        'void ares_destroy_options(struct ares_options *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_dup():
        'int ares_dup(struct ares_channeldata * *, struct ares_channeldata *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_expand_name():
        'int ares_expand_name(unsigned char *, unsigned char *, int, char * *, long *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_expand_string():
        'int ares_expand_string(unsigned char *, unsigned char *, int, unsigned char * *, long *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_free_data():
        'void ares_free_data(void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_free_hostent():
        'void ares_free_hostent(struct hostent *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_free_string():
        'void ares_free_string(void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_get_servers():
        'int ares_get_servers(struct ares_channeldata *, struct ares_addr_node * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_gethostbyaddr():
        'void ares_gethostbyaddr(struct ares_channeldata *, void *, int, int, void(*)(void *, int, int, struct hostent *), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_gethostbyname():
        'void ares_gethostbyname(struct ares_channeldata *, char *, int, void(*)(void *, int, int, struct hostent *), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_gethostbyname_file():
        'int ares_gethostbyname_file(struct ares_channeldata *, char *, int, struct hostent * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_getnameinfo():
        'void ares_getnameinfo(struct ares_channeldata *, struct sockaddr *, uint32_t, int, void(*)(void *, int, int, char *, char *), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_getsock():
        'int ares_getsock(struct ares_channeldata *, int32_t *, int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_inet_ntop():
        'char *ares_inet_ntop(int, void *, char *, uint32_t);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_inet_pton():
        'int ares_inet_pton(int, char *, void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_init():
        'int ares_init(struct ares_channeldata * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_init_options():
        'int ares_init_options(struct ares_channeldata * *, struct ares_options *, int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_library_cleanup():
        'void ares_library_cleanup();\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_library_init():
        'int ares_library_init(int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_mkquery():
        'int ares_mkquery(char *, int, int, unsigned short, int, unsigned char * *, int *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_a_reply():
        'int ares_parse_a_reply(unsigned char *, int, struct hostent * *, struct ares_addrttl *, int *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_aaaa_reply():
        'int ares_parse_aaaa_reply(unsigned char *, int, struct hostent * *, struct ares_addr6ttl *, int *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_mx_reply():
        'int ares_parse_mx_reply(unsigned char *, int, struct ares_mx_reply * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_naptr_reply():
        'int ares_parse_naptr_reply(unsigned char *, int, struct ares_naptr_reply * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_ns_reply():
        'int ares_parse_ns_reply(unsigned char *, int, struct hostent * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_ptr_reply():
        'int ares_parse_ptr_reply(unsigned char *, int, void *, int, int, struct hostent * *, int *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_soa_reply():
        'int ares_parse_soa_reply(unsigned char *, int, struct ares_soa_reply * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_srv_reply():
        'int ares_parse_srv_reply(unsigned char *, int, struct ares_srv_reply * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_parse_txt_reply_ext():
        'int ares_parse_txt_reply_ext(unsigned char *, int, struct ares_txt_ext * *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_process_fd():
        'void ares_process_fd(struct ares_channeldata *, int32_t, int32_t);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_query():
        'void ares_query(struct ares_channeldata *, char *, int, int, void(*)(void *, int, int, unsigned char *, int), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_save_options():
        'int ares_save_options(struct ares_channeldata *, struct ares_options *, int *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_search():
        'void ares_search(struct ares_channeldata *, char *, int, int, void(*)(void *, int, int, unsigned char *, int), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_send():
        'void ares_send(struct ares_channeldata *, unsigned char *, int, void(*)(void *, int, int, unsigned char *, int), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_set_local_dev():
        'void ares_set_local_dev(struct ares_channeldata *, char *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_set_local_ip4():
        'void ares_set_local_ip4(struct ares_channeldata *, unsigned int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_set_local_ip6():
        'void ares_set_local_ip6(struct ares_channeldata *, unsigned char *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_set_servers():
        'int ares_set_servers(struct ares_channeldata *, struct ares_addr_node *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_set_socket_callback():
        'void ares_set_socket_callback(struct ares_channeldata *, int(*)(int32_t, int, void *), void *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_strerror():
        'char *ares_strerror(int);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_timeout():
        'struct timeval *ares_timeout(struct ares_channeldata *, struct timeval *, struct timeval *);\n\nCFFI C function from _cares.lib'
        pass
    
    @staticmethod
    def ares_version():
        'char *ares_version(int *);\n\nCFFI C function from _cares.lib'
        pass
    

