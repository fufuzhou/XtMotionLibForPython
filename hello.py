import ctypes
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import C_SoftLanding_dll

# dl = ctypes.cdll.LoadLibrary("./MotionControlDll.dll")
#
# dl.Ping.restype = ctypes.c_int
# dl.Ping.argtypes = [ctypes.c_wchar_p]
#
# dl.InitDevice_PC_Local_Controler.restype = None
# dl.InitDevice_PC_Local_Controler.argtypes = [ctypes.c_int]
#
#
# dl.InitDevice_PC_Local_Controler(0)
ins = ctypes.c_wchar_p('127.0.0.1')
print(ins)
# res = dl.Ping(ins)
# print(res)

msg = "Hello World"
print(msg)

x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show()
