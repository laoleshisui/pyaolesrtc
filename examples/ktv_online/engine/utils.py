import ctypes


def GetData(c_voidptr, length):
    c_void_p_obj = ctypes.c_void_p(int(c_voidptr))
    pointer_arr = ctypes.cast(c_void_p_obj, ctypes.POINTER(ctypes.c_ubyte * length))
    return pointer_arr.contents