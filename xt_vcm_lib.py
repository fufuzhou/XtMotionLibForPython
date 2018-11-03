#_*_ coding:UTF-8 _*_
import ctypes
class VCM_Resource_struct(ctypes.Structure):
    'VCM_Resource_struct 的 Python 版本'
    _fields_ = [
        ("CanID",ctypes.c_int),
        ("iAxis",ctypes.c_int),
        ("IO_ID",ctypes.c_int),
        ("iThread",ctypes.c_int),
        ("iThread_Curve",ctypes.c_int),
        ("Connet_Rebuild",ctypes.c_int)
    ]

vcm = ctypes.cdll.LoadLibrary("./voice_motor_dll.dll")

# 初始化并加载音圈控制端，motor_num == 音圈电机数量（音圈电机 id=1~15）
vcm.Soft_landing_dll_init.restype = None
vcm.Soft_landing_dll_init.argtypes = [ctypes.c_int]

# 设置电机运动正方向 direct == 0 正向 direct == 1反向
vcm.SetRunDirect.restype = None
vcm.SetRunDirect.argtypes = [ctypes.c_int, ctypes.c_int]

#手动分配电机资源
vcm.VCMT_resource_alloc.restype = None
vcm.VCMT_resource_alloc.argtypes = [ctypes.POINTER(VCM_Resource_struct), ctypes.c_int]

#获取音圈电机初始化状态，成功返回1，忙返回0,电机不存在返回 -1。
vcm.Get_Init_Ready.restype = ctypes.c_int
vcm.Get_Init_Ready.argtype = None

#显示调试窗体,卡死并等待调试窗体返回
vcm.ShowSettingDlg.restype = None
vcm.ShowSettingDlg.argtype = None

#释放音圈控制端
vcm.Soft_landing_dll_uninit.restype = None
vcm.Soft_landing_dll_uninit.argtype = None

#进行软着陆运动(motor_id = 音圈电机id 1~15)
#成功返回0 失败返回起点不一致计数器
vcm.Do_Softlanding.resttpe = ctypes.c_int
vcm.Do_Softlanding.argtype = ctypes.c_int

#使用指定的轨迹槽slot =0~9(10轨迹槽)
#默认使用0号槽
#用于快速切换轨迹槽,不需要重新计算插补参数。
vcm.SetSoftlandingSlot.restype = None
vcm.SetSoftlandingSlot.argtype = [ctypes.c_int,ctypes.c_int]

#进行软着陆运动(motor_id = 音圈电机id 1~15)
#成功返回0 失败返回起点不一致计数器
vcm.Do_SoftDown.restype = ctypes.c_int
vcm.Do_SoftDown.argtype = ctypes.c_int

#进行软着陆运动回位(motor_id = 音圈电机id 1~15)
#成功返回0 失败返回起点不一致计数器
vcm.Do_SoftUp.restype = ctypes.c_int
vcm.Do_SoftUp.argtype = ctypes.c_int

#获取电机软着陆运动状态(motor_id = 音圈电机id 1~15)
#flag_index代码 busy_flag_down == 0 busy_flag_up == 1
#忙返回1 空闲返回0 电机不存在返回 -1
#用于软着陆模式
vcm.Get_Busy.restype = ctypes.c_int
vcm.Get_Busy.argtype = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

#获取错误码
#  error_over_current 1
#  error_go_zero (1<<1)
#  error_over_temp (1<<2)
#  error_leakage_current (1<<3)
#控制器错误返回-1
#处理方法同GetControllerError
vcm.get_motor_error.restype = ctypes.c_int64
vcm.get_motor_error.argtype = ctypes.c_int


#回零位
#回零成功返回1 失败返回0 超时返回-1
#需要返回错误（类型）
#阻塞 成功或者失败后返回
vcm.Init_Go_Zero.restype = ctypes.c_int
vcm.Init_Go_Zero.argtype = ctypes.c_int

#/获取当前原点开关信号
vcm.GetZeroIO.restype = ctypes.c_int
vcm.GetZeroIO.argtype = ctypes.c_int

#设定零位偏移
vcm.GetZeroIO.restype = None
vcm.GetZeroIO.argtype = [ctypes.c_int,ctypes.c_double]

# //位置控制模式的运动函数
# //设置位置模式限位
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int SetPosLimit(int motor_id,double max_pos,double min_pos);
#
# //设置位置模式加加速度
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int SetPosModejerk(int motor_id, double jerk);
#
# //设置位置模式加速度
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int SetPosModeAcc(int motor_id, double Acc);
#
# //设置位置模式速度
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int SetPosModeSpeed(int motor_id, double speed);
#
# //设置目标并运动到指定位置
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int SetPosModePos(int motor_id, double Pos);
#
# //等待运动停止
# //成功返回1 失败返回0
# //wait_user == 1 用户程序等待 wait_user == 0 内部指令等待
# EXTERNC _DLLAPI int TillPosModePos(int motor_id, int wait_user);
#
# //获取指令缓冲长度
# EXTERNC _DLLAPI int GetInsBuffLen(int motor_id);
#
#
# //增量运动
# EXTERNC _DLLAPI void SGO_INCREASE(int motor_id, double Pos);
#
# //插入延迟指令
# EXTERNC _DLLAPI void AddMotorDelay(int motor_id, double time_ms);
#
# //获取当前磁栅尺真实位置，成功返回1。
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int GetNowPos(int motor_id, double &Pos);
#
# //获取控制器输出位置，成功返回1。
# //成功返回1 失败返回0
# EXTERNC _DLLAPI int GetTargetPos(int motor_id, double &Pos);
#
# //获取到位信号 到位返回1 运动中返回0
# //用于位置模式
# EXTERNC _DLLAPI int CheckPosReady(int motor_id);
#
# //设定最大最小电流限制（推电流MaxI<=10A,拉电流MinI>=-10A）
# EXTERNC _DLLAPI int SetCurrentLimit(int motor_id,double MaxI,double MinI);
#
# EXTERNC _DLLAPI int SetDelay(int motor_id, int ms);
#
#
#
# //软着陆函数
# //设定快速进给速度
# EXTERNC _DLLAPI void SetFastSpeed(int motor_id, double speed);
# //设定快速进给加速度
# EXTERNC _DLLAPI void SetFastAcc(int motor_id,double Acc);
# //设定慢速接近速度
# EXTERNC _DLLAPI void SetSlowSpeed(int motor_id,double speed);
# //设定慢速接近加速度
# EXTERNC _DLLAPI void SetSlowAcc(int motor_id, double Acc);
# //设定软着陆力
# EXTERNC _DLLAPI void SetForce(int motor_id,double force);
# //设定软着陆位置
# EXTERNC _DLLAPI void SetSoftPos(int motor_id, double pos);
#
# //设定软着陆余量
# EXTERNC _DLLAPI void SetSoftLandingMargin(int motor_id, double margin);
#
#
#
#
# //获取当前轨迹槽的然着陆运动时间
# EXTERNC _DLLAPI	double GetSoftlandingTime(int motor_id);
# //更新软着陆参数至当前轨迹槽
# EXTERNC _DLLAPI void UpdataParam(int motor_id);
#
# //返回设定软着陆位置s，单位mm,(motor_id = 音圈电机id 1~15)
# //返回位置
# //bug待修正
# EXTERNC _DLLAPI	double Get_Softlanding_endpos(int motor_id);
#
#
# //获取控制服务端错误码 ==1 则需要析构后重构
# //检测控制卡服务端状态
# EXTERNC _DLLAPI	int GetControllerError(void);
#
# //减速急停
# EXTERNC _DLLAPI	void StopVmc(int motor_id);
#
#
# //计算并生成电流和力的映射表（自动插值,需要len>3）
# //m_Current电流（单位A）  m_Force力（单位g）
# EXTERNC _DLLAPI	void MapCurrent2Force(int motor_id, double *m_Current, double *m_Force, int len);