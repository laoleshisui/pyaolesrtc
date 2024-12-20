# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.0
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
import sys
import platform

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    os_name = sys.platform
    cpu_arch = platform.machine()
    if os_name == 'darwin':
        from .lib.darwin.arm64 import _aolesrtc_python_api
    elif os_name == 'linux':
        from .lib.darwin.x86_x64 import _aolesrtc_python_api
    else:
        print(f'current os is not supportted :', os_name, cpu_arch)
else:
    import _aolesrtc_python_api

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aolesrtc_python_api.delete_SwigPyIterator

    def value(self):
        return _aolesrtc_python_api.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _aolesrtc_python_api.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _aolesrtc_python_api.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _aolesrtc_python_api.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _aolesrtc_python_api.SwigPyIterator_equal(self, x)

    def copy(self):
        return _aolesrtc_python_api.SwigPyIterator_copy(self)

    def next(self):
        return _aolesrtc_python_api.SwigPyIterator_next(self)

    def __next__(self):
        return _aolesrtc_python_api.SwigPyIterator___next__(self)

    def previous(self):
        return _aolesrtc_python_api.SwigPyIterator_previous(self)

    def advance(self, n):
        return _aolesrtc_python_api.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _aolesrtc_python_api.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _aolesrtc_python_api.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _aolesrtc_python_api.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _aolesrtc_python_api.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _aolesrtc_python_api.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _aolesrtc_python_api.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _aolesrtc_python_api:
_aolesrtc_python_api.SwigPyIterator_swigregister(SwigPyIterator)
class Controller(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _aolesrtc_python_api.Controller_swiginit(self, _aolesrtc_python_api.new_Controller())
    __swig_destroy__ = _aolesrtc_python_api.delete_Controller

    @staticmethod
    def LoadConfigFromServer(server):
        return _aolesrtc_python_api.Controller_LoadConfigFromServer(server)

    @staticmethod
    def LoadConfigString(config_content):
        return _aolesrtc_python_api.Controller_LoadConfigString(config_content)

    @staticmethod
    def LoadConfigFile(config_file):
        return _aolesrtc_python_api.Controller_LoadConfigFile(config_file)

    @staticmethod
    def InitLog(*args):
        return _aolesrtc_python_api.Controller_InitLog(*args)

    def Get(self):
        return _aolesrtc_python_api.Controller_Get(self)

# Register Controller in _aolesrtc_python_api:
_aolesrtc_python_api.Controller_swigregister(Controller)
class DataOutput(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, type):
        if self.__class__ == DataOutput:
            _self = None
        else:
            _self = self
        _aolesrtc_python_api.DataOutput_swiginit(self, _aolesrtc_python_api.new_DataOutput(_self, type))

    def OnDataYUVOut(self, id, width, height, data_y, stride_y, data_u, stride_u, data_v, stride_v):
        return _aolesrtc_python_api.DataOutput_OnDataYUVOut(self, id, width, height, data_y, stride_y, data_u, stride_u, data_v, stride_v)

    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        return _aolesrtc_python_api.DataOutput_OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames)
    __swig_destroy__ = _aolesrtc_python_api.delete_DataOutput
    def __disown__(self):
        self.this.disown()
        _aolesrtc_python_api.disown_DataOutput(self)
        return weakref.proxy(self)

# Register DataOutput in _aolesrtc_python_api:
_aolesrtc_python_api.DataOutput_swigregister(DataOutput)
class DataInput(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, type):
        _aolesrtc_python_api.DataInput_swiginit(self, _aolesrtc_python_api.new_DataInput(type))

    def SetState(self, is_live):
        return _aolesrtc_python_api.DataInput_SetState(self, is_live)

    def SetAdaption(self, adaption):
        return _aolesrtc_python_api.DataInput_SetAdaption(self, adaption)

    def AdaptOutputFormat(self, landscape_width, landscape_height, max_landscape_pixel_count, portrait_width, portrait_height, max_portrait_pixel_count, max_fps):
        return _aolesrtc_python_api.DataInput_AdaptOutputFormat(self, landscape_width, landscape_height, max_landscape_pixel_count, portrait_width, portrait_height, max_portrait_pixel_count, max_fps)

    def OnDataYUVIn(self, *args):
        return _aolesrtc_python_api.DataInput_OnDataYUVIn(self, *args)

    def OnDataAudioIn(self, *args):
        return _aolesrtc_python_api.DataInput_OnDataAudioIn(self, *args)
    __swig_destroy__ = _aolesrtc_python_api.delete_DataInput

# Register DataInput in _aolesrtc_python_api:
_aolesrtc_python_api.DataInput_swigregister(DataInput)

def cast_ptr_void(p):
    return _aolesrtc_python_api.cast_ptr_void(p)

def cast_ptr_uint8_t(p):
    return _aolesrtc_python_api.cast_ptr_uint8_t(p)
DataIOType_NONE = _aolesrtc_python_api.DataIOType_NONE
DataIOType_I420 = _aolesrtc_python_api.DataIOType_I420
DataIOType_I422 = _aolesrtc_python_api.DataIOType_I422
DataIOType_I444 = _aolesrtc_python_api.DataIOType_I444
DataIOType_AUDIO = _aolesrtc_python_api.DataIOType_AUDIO
class DataIO(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, type):
        _aolesrtc_python_api.DataIO_swiginit(self, _aolesrtc_python_api.new_DataIO(type))
    __swig_destroy__ = _aolesrtc_python_api.delete_DataIO

    def Type(self):
        return _aolesrtc_python_api.DataIO_Type(self)

    def SetType(self, type):
        return _aolesrtc_python_api.DataIO_SetType(self, type)

    def IO(self):
        return _aolesrtc_python_api.DataIO_IO(self)

    def SetIO(self, io_impl):
        return _aolesrtc_python_api.DataIO_SetIO(self, io_impl)

# Register DataIO in _aolesrtc_python_api:
_aolesrtc_python_api.DataIO_swigregister(DataIO)
class DataIOFactory(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, controller):
        _aolesrtc_python_api.DataIOFactory_swiginit(self, _aolesrtc_python_api.new_DataIOFactory(controller))
    __swig_destroy__ = _aolesrtc_python_api.delete_DataIOFactory

    def CreateDataIOSource(self, type):
        return _aolesrtc_python_api.DataIOFactory_CreateDataIOSource(self, type)

    def CreateDataIOSink(self, *args):
        return _aolesrtc_python_api.DataIOFactory_CreateDataIOSink(self, *args)

# Register DataIOFactory in _aolesrtc_python_api:
_aolesrtc_python_api.DataIOFactory_swigregister(DataIOFactory)
class P2PModuleObserver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def OnConnEvent(self, ok):
        return _aolesrtc_python_api.P2PModuleObserver_OnConnEvent(self, ok)

    def OnLoginEvent(self, ok, id):
        return _aolesrtc_python_api.P2PModuleObserver_OnLoginEvent(self, ok, id)

    def __init__(self):
        if self.__class__ == P2PModuleObserver:
            _self = None
        else:
            _self = self
        _aolesrtc_python_api.P2PModuleObserver_swiginit(self, _aolesrtc_python_api.new_P2PModuleObserver(_self, ))
    __swig_destroy__ = _aolesrtc_python_api.delete_P2PModuleObserver
    def __disown__(self):
        self.this.disown()
        _aolesrtc_python_api.disown_P2PModuleObserver(self)
        return weakref.proxy(self)

# Register P2PModuleObserver in _aolesrtc_python_api:
_aolesrtc_python_api.P2PModuleObserver_swigregister(P2PModuleObserver)
class P2PClientDataIO(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, controller):
        _aolesrtc_python_api.P2PClientDataIO_swiginit(self, _aolesrtc_python_api.new_P2PClientDataIO(controller))

    def AddLocalVideoSource(self, label, source):
        return _aolesrtc_python_api.P2PClientDataIO_AddLocalVideoSource(self, label, source)

    def AddLocalAudioSource(self, label, source=None):
        return _aolesrtc_python_api.P2PClientDataIO_AddLocalAudioSource(self, label, source)

    def AddLocalVideoSink(self, label, sink):
        return _aolesrtc_python_api.P2PClientDataIO_AddLocalVideoSink(self, label, sink)

    def AddRemoteVideoSink(self, label, sink):
        return _aolesrtc_python_api.P2PClientDataIO_AddRemoteVideoSink(self, label, sink)

    def AddLocalAudioSink(self, label, sink):
        return _aolesrtc_python_api.P2PClientDataIO_AddLocalAudioSink(self, label, sink)

    def AddRemoteAudioSink(self, label, sink):
        return _aolesrtc_python_api.P2PClientDataIO_AddRemoteAudioSink(self, label, sink)

    def Login(self):
        return _aolesrtc_python_api.P2PClientDataIO_Login(self)

    def ConnectToPeer(self, id):
        return _aolesrtc_python_api.P2PClientDataIO_ConnectToPeer(self, id)

    def Close(self):
        return _aolesrtc_python_api.P2PClientDataIO_Close(self)

    def SetAudioPlayout(self, playout):
        return _aolesrtc_python_api.P2PClientDataIO_SetAudioPlayout(self, playout)

    def AddP2PModuleObserver(self, observer):
        return _aolesrtc_python_api.P2PClientDataIO_AddP2PModuleObserver(self, observer)
    __swig_destroy__ = _aolesrtc_python_api.delete_P2PClientDataIO

# Register P2PClientDataIO in _aolesrtc_python_api:
_aolesrtc_python_api.P2PClientDataIO_swigregister(P2PClientDataIO)
class ServiceDetail(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_aolesrtc_python_api.ServiceDetail_name_get, _aolesrtc_python_api.ServiceDetail_name_set)
    description = property(_aolesrtc_python_api.ServiceDetail_description_get, _aolesrtc_python_api.ServiceDetail_description_set)
    ip = property(_aolesrtc_python_api.ServiceDetail_ip_get, _aolesrtc_python_api.ServiceDetail_ip_set)
    port = property(_aolesrtc_python_api.ServiceDetail_port_get, _aolesrtc_python_api.ServiceDetail_port_set)

    def __init__(self):
        _aolesrtc_python_api.ServiceDetail_swiginit(self, _aolesrtc_python_api.new_ServiceDetail())
    __swig_destroy__ = _aolesrtc_python_api.delete_ServiceDetail

# Register ServiceDetail in _aolesrtc_python_api:
_aolesrtc_python_api.ServiceDetail_swigregister(ServiceDetail)
class JanusCenterObserver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def OnGetJanus(self, *args):
        return _aolesrtc_python_api.JanusCenterObserver_OnGetJanus(self, *args)

    def __init__(self):
        if self.__class__ == JanusCenterObserver:
            _self = None
        else:
            _self = self
        _aolesrtc_python_api.JanusCenterObserver_swiginit(self, _aolesrtc_python_api.new_JanusCenterObserver(_self, ))
    __swig_destroy__ = _aolesrtc_python_api.delete_JanusCenterObserver
    def __disown__(self):
        self.this.disown()
        _aolesrtc_python_api.disown_JanusCenterObserver(self)
        return weakref.proxy(self)

# Register JanusCenterObserver in _aolesrtc_python_api:
_aolesrtc_python_api.JanusCenterObserver_swigregister(JanusCenterObserver)
class JanusCenterClient(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, controller):
        _aolesrtc_python_api.JanusCenterClient_swiginit(self, _aolesrtc_python_api.new_JanusCenterClient(controller))
    __swig_destroy__ = _aolesrtc_python_api.delete_JanusCenterClient

    def GetJanus(self, refresh=False):
        return _aolesrtc_python_api.JanusCenterClient_GetJanus(self, refresh)

    def AddObserver(self, observer):
        return _aolesrtc_python_api.JanusCenterClient_AddObserver(self, observer)

# Register JanusCenterClient in _aolesrtc_python_api:
_aolesrtc_python_api.JanusCenterClient_swigregister(JanusCenterClient)
class VideoRoomClientObserver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def OnJsep(self, type, sdp):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnJsep(self, type, sdp)

    def OnCreateRoom(self, handler_id, room_id):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnCreateRoom(self, handler_id, room_id)

    def OnListRooms(self, handler_id, room_infos):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnListRooms(self, handler_id, room_infos)

    def OnListParticipants(self, handler_id, room_id, room_participants):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnListParticipants(self, handler_id, room_id, room_participants)

    def OnJoinAsPublisher(self, handler_id, room_id, publisher_id):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnJoinAsPublisher(self, handler_id, room_id, publisher_id)

    def OnJoinAsSubscriber(self, handler_id, room_id):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnJoinAsSubscriber(self, handler_id, room_id)

    def OnLeave(self, handler_id, room_id, publisher_id):
        return _aolesrtc_python_api.VideoRoomClientObserver_OnLeave(self, handler_id, room_id, publisher_id)

    def __init__(self):
        if self.__class__ == VideoRoomClientObserver:
            _self = None
        else:
            _self = self
        _aolesrtc_python_api.VideoRoomClientObserver_swiginit(self, _aolesrtc_python_api.new_VideoRoomClientObserver(_self, ))
    __swig_destroy__ = _aolesrtc_python_api.delete_VideoRoomClientObserver
    def __disown__(self):
        self.this.disown()
        _aolesrtc_python_api.disown_VideoRoomClientObserver(self)
        return weakref.proxy(self)

# Register VideoRoomClientObserver in _aolesrtc_python_api:
_aolesrtc_python_api.VideoRoomClientObserver_swigregister(VideoRoomClientObserver)
class UINT64Vector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _aolesrtc_python_api.UINT64Vector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _aolesrtc_python_api.UINT64Vector___nonzero__(self)

    def __bool__(self):
        return _aolesrtc_python_api.UINT64Vector___bool__(self)

    def __len__(self):
        return _aolesrtc_python_api.UINT64Vector___len__(self)

    def __getslice__(self, i, j):
        return _aolesrtc_python_api.UINT64Vector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _aolesrtc_python_api.UINT64Vector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _aolesrtc_python_api.UINT64Vector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _aolesrtc_python_api.UINT64Vector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _aolesrtc_python_api.UINT64Vector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _aolesrtc_python_api.UINT64Vector___setitem__(self, *args)

    def pop(self):
        return _aolesrtc_python_api.UINT64Vector_pop(self)

    def append(self, x):
        return _aolesrtc_python_api.UINT64Vector_append(self, x)

    def empty(self):
        return _aolesrtc_python_api.UINT64Vector_empty(self)

    def size(self):
        return _aolesrtc_python_api.UINT64Vector_size(self)

    def swap(self, v):
        return _aolesrtc_python_api.UINT64Vector_swap(self, v)

    def begin(self):
        return _aolesrtc_python_api.UINT64Vector_begin(self)

    def end(self):
        return _aolesrtc_python_api.UINT64Vector_end(self)

    def rbegin(self):
        return _aolesrtc_python_api.UINT64Vector_rbegin(self)

    def rend(self):
        return _aolesrtc_python_api.UINT64Vector_rend(self)

    def clear(self):
        return _aolesrtc_python_api.UINT64Vector_clear(self)

    def get_allocator(self):
        return _aolesrtc_python_api.UINT64Vector_get_allocator(self)

    def pop_back(self):
        return _aolesrtc_python_api.UINT64Vector_pop_back(self)

    def erase(self, *args):
        return _aolesrtc_python_api.UINT64Vector_erase(self, *args)

    def __init__(self, *args):
        _aolesrtc_python_api.UINT64Vector_swiginit(self, _aolesrtc_python_api.new_UINT64Vector(*args))

    def push_back(self, x):
        return _aolesrtc_python_api.UINT64Vector_push_back(self, x)

    def front(self):
        return _aolesrtc_python_api.UINT64Vector_front(self)

    def back(self):
        return _aolesrtc_python_api.UINT64Vector_back(self)

    def assign(self, n, x):
        return _aolesrtc_python_api.UINT64Vector_assign(self, n, x)

    def resize(self, *args):
        return _aolesrtc_python_api.UINT64Vector_resize(self, *args)

    def insert(self, *args):
        return _aolesrtc_python_api.UINT64Vector_insert(self, *args)

    def reserve(self, n):
        return _aolesrtc_python_api.UINT64Vector_reserve(self, n)

    def capacity(self):
        return _aolesrtc_python_api.UINT64Vector_capacity(self)
    __swig_destroy__ = _aolesrtc_python_api.delete_UINT64Vector

# Register UINT64Vector in _aolesrtc_python_api:
_aolesrtc_python_api.UINT64Vector_swigregister(UINT64Vector)
class UINT8Vector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _aolesrtc_python_api.UINT8Vector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _aolesrtc_python_api.UINT8Vector___nonzero__(self)

    def __bool__(self):
        return _aolesrtc_python_api.UINT8Vector___bool__(self)

    def __len__(self):
        return _aolesrtc_python_api.UINT8Vector___len__(self)

    def __getslice__(self, i, j):
        return _aolesrtc_python_api.UINT8Vector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _aolesrtc_python_api.UINT8Vector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _aolesrtc_python_api.UINT8Vector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _aolesrtc_python_api.UINT8Vector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _aolesrtc_python_api.UINT8Vector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _aolesrtc_python_api.UINT8Vector___setitem__(self, *args)

    def pop(self):
        return _aolesrtc_python_api.UINT8Vector_pop(self)

    def append(self, x):
        return _aolesrtc_python_api.UINT8Vector_append(self, x)

    def empty(self):
        return _aolesrtc_python_api.UINT8Vector_empty(self)

    def size(self):
        return _aolesrtc_python_api.UINT8Vector_size(self)

    def swap(self, v):
        return _aolesrtc_python_api.UINT8Vector_swap(self, v)

    def begin(self):
        return _aolesrtc_python_api.UINT8Vector_begin(self)

    def end(self):
        return _aolesrtc_python_api.UINT8Vector_end(self)

    def rbegin(self):
        return _aolesrtc_python_api.UINT8Vector_rbegin(self)

    def rend(self):
        return _aolesrtc_python_api.UINT8Vector_rend(self)

    def clear(self):
        return _aolesrtc_python_api.UINT8Vector_clear(self)

    def get_allocator(self):
        return _aolesrtc_python_api.UINT8Vector_get_allocator(self)

    def pop_back(self):
        return _aolesrtc_python_api.UINT8Vector_pop_back(self)

    def erase(self, *args):
        return _aolesrtc_python_api.UINT8Vector_erase(self, *args)

    def __init__(self, *args):
        _aolesrtc_python_api.UINT8Vector_swiginit(self, _aolesrtc_python_api.new_UINT8Vector(*args))

    def push_back(self, x):
        return _aolesrtc_python_api.UINT8Vector_push_back(self, x)

    def front(self):
        return _aolesrtc_python_api.UINT8Vector_front(self)

    def back(self):
        return _aolesrtc_python_api.UINT8Vector_back(self)

    def assign(self, n, x):
        return _aolesrtc_python_api.UINT8Vector_assign(self, n, x)

    def resize(self, *args):
        return _aolesrtc_python_api.UINT8Vector_resize(self, *args)

    def insert(self, *args):
        return _aolesrtc_python_api.UINT8Vector_insert(self, *args)

    def reserve(self, n):
        return _aolesrtc_python_api.UINT8Vector_reserve(self, n)

    def capacity(self):
        return _aolesrtc_python_api.UINT8Vector_capacity(self)
    __swig_destroy__ = _aolesrtc_python_api.delete_UINT8Vector

# Register UINT8Vector in _aolesrtc_python_api:
_aolesrtc_python_api.UINT8Vector_swigregister(UINT8Vector)
class JanusVideoRoomClientDataIO(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, controller):
        _aolesrtc_python_api.JanusVideoRoomClientDataIO_swiginit(self, _aolesrtc_python_api.new_JanusVideoRoomClientDataIO(controller))

    def AddLocalVideoSource(self, label, source):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddLocalVideoSource(self, label, source)

    def AddLocalAudioSource(self, label, source=None):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddLocalAudioSource(self, label, source)

    def AddLocalVideoSink(self, label, sink):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddLocalVideoSink(self, label, sink)

    def AddRemoteVideoSink(self, label, sink):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddRemoteVideoSink(self, label, sink)

    def AddLocalAudioSink(self, label, sink):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddLocalAudioSink(self, label, sink)

    def AddRemoteAudioSink(self, label, sink):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddRemoteAudioSink(self, label, sink)

    def CreateSession(self, server):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_CreateSession(self, server)

    def CreateRoom(self, room_id, description):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_CreateRoom(self, room_id, description)

    def ListRooms(self):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_ListRooms(self)

    def ListParticipants(self, room_id):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_ListParticipants(self, room_id)

    def Publish(self, room_id, pub_id, display):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_Publish(self, room_id, pub_id, display)

    def Subscribe(self, room_id, feeds):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_Subscribe(self, room_id, feeds)

    def UpdateSubscriptions(self, room_id, sub_publishers_id, unsub_publishers_id):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_UpdateSubscriptions(self, room_id, sub_publishers_id, unsub_publishers_id)

    def LeaveRoom(self, room_id):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_LeaveRoom(self, room_id)

    def SetAudioPlayout(self, playout):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_SetAudioPlayout(self, playout)

    def AddVideoRoomClientObserver(self, observer):
        return _aolesrtc_python_api.JanusVideoRoomClientDataIO_AddVideoRoomClientObserver(self, observer)
    __swig_destroy__ = _aolesrtc_python_api.delete_JanusVideoRoomClientDataIO

# Register JanusVideoRoomClientDataIO in _aolesrtc_python_api:
_aolesrtc_python_api.JanusVideoRoomClientDataIO_swigregister(JanusVideoRoomClientDataIO)
class JanusAudioBridgeClient(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, controller):
        _aolesrtc_python_api.JanusAudioBridgeClient_swiginit(self, _aolesrtc_python_api.new_JanusAudioBridgeClient(controller))
    __swig_destroy__ = _aolesrtc_python_api.delete_JanusAudioBridgeClient

    def AddLocalAudioSource(self, label, source=None):
        return _aolesrtc_python_api.JanusAudioBridgeClient_AddLocalAudioSource(self, label, source)

    def AddLocalAudioSink(self, label, sink):
        return _aolesrtc_python_api.JanusAudioBridgeClient_AddLocalAudioSink(self, label, sink)

    def AddRemoteAudioSink(self, label, sink):
        return _aolesrtc_python_api.JanusAudioBridgeClient_AddRemoteAudioSink(self, label, sink)

    def SetAudioPlayout(self, playout):
        return _aolesrtc_python_api.JanusAudioBridgeClient_SetAudioPlayout(self, playout)

    def AddObserver(self, observer):
        return _aolesrtc_python_api.JanusAudioBridgeClient_AddObserver(self, observer)

    def CreateSession(self, server):
        return _aolesrtc_python_api.JanusAudioBridgeClient_CreateSession(self, server)

    def CreateRoom(self, room_id):
        return _aolesrtc_python_api.JanusAudioBridgeClient_CreateRoom(self, room_id)

    def DestroyRoom(self, room_id, secret):
        return _aolesrtc_python_api.JanusAudioBridgeClient_DestroyRoom(self, room_id, secret)

    def ListRooms(self):
        return _aolesrtc_python_api.JanusAudioBridgeClient_ListRooms(self)

    def ListParticipants(self, room_id):
        return _aolesrtc_python_api.JanusAudioBridgeClient_ListParticipants(self, room_id)

    def Join(self, room_id, id, display, pin, muted):
        return _aolesrtc_python_api.JanusAudioBridgeClient_Join(self, room_id, id, display, pin, muted)

    def Configure(self, display, muted):
        return _aolesrtc_python_api.JanusAudioBridgeClient_Configure(self, display, muted)

    def ConfigureWithOffer(self):
        return _aolesrtc_python_api.JanusAudioBridgeClient_ConfigureWithOffer(self)

    def ConfigureWithoutOffer(self):
        return _aolesrtc_python_api.JanusAudioBridgeClient_ConfigureWithoutOffer(self)

    def ChangeRoom(self, room_id, id, display):
        return _aolesrtc_python_api.JanusAudioBridgeClient_ChangeRoom(self, room_id, id, display)

    def LeaveRoom(self, room_id):
        return _aolesrtc_python_api.JanusAudioBridgeClient_LeaveRoom(self, room_id)

# Register JanusAudioBridgeClient in _aolesrtc_python_api:
_aolesrtc_python_api.JanusAudioBridgeClient_swigregister(JanusAudioBridgeClient)
class AudioBridgeClientObserver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def OnJsep(self, type, sdp):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnJsep(self, type, sdp)

    def OnCreateRoom(self, handler_id, room_id):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnCreateRoom(self, handler_id, room_id)

    def OnListRooms(self, handler_id, room_infos):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnListRooms(self, handler_id, room_infos)

    def OnListParticipants(self, handler_id, room_id, room_participants):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnListParticipants(self, handler_id, room_id, room_participants)

    def OnJoin(self, handler_id, room_id, id):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnJoin(self, handler_id, room_id, id)

    def OnLeave(self, handler_id, room_id, id):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnLeave(self, handler_id, room_id, id)

    def OnDestroy(self, handler_id, room_id):
        return _aolesrtc_python_api.AudioBridgeClientObserver_OnDestroy(self, handler_id, room_id)

    def __init__(self):
        if self.__class__ == AudioBridgeClientObserver:
            _self = None
        else:
            _self = self
        _aolesrtc_python_api.AudioBridgeClientObserver_swiginit(self, _aolesrtc_python_api.new_AudioBridgeClientObserver(_self, ))
    __swig_destroy__ = _aolesrtc_python_api.delete_AudioBridgeClientObserver
    def __disown__(self):
        self.this.disown()
        _aolesrtc_python_api.disown_AudioBridgeClientObserver(self)
        return weakref.proxy(self)

# Register AudioBridgeClientObserver in _aolesrtc_python_api:
_aolesrtc_python_api.AudioBridgeClientObserver_swigregister(AudioBridgeClientObserver)

