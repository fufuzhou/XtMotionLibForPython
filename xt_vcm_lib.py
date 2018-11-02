import ctypes

vcm = ctypes.cdll.LoadLibrary("./voice_motor_dll.dll")

# 初始化并加载音圈控制端，motor_num == 音圈电机数量（音圈电机 id=1~15）
vcm.Soft_landing_dll_init.restype = None
vcm.Soft_landing_dll_init.argtypes = [ctypes.c_int]

# 设置电机运动正方向 direct == 0 正向 direct == 1反向
vcm.SetRunDirect.restype = None
vcm.SetRunDirect.argtypes = [ctypes.c_int,ctypes.c_int]