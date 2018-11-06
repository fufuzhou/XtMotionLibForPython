# _*_ coding:UTF-8 _*_
from ctypes import *
C_SoftLanding_dll = cdll.LoadLibrary("./voice_motor_dll.dll")

class VCM_Resource_struct(Structure):
    'VCM_Resource_struct 的 Python 版本'
    _fields_ = [
        ("CanID", c_int),
        ("iAxis", c_int),
        ("IO_ID", c_int),
        ("iThread", c_int),
        ("iThread_Curve", c_int),
        ("Connet_Rebuild", c_int)
    ]

# #pragma once
# #include "VCM_init_Struct.h"
# //sugar 2018-8-7
# #ifdef _DLLAPI
# #undef _DLLAPI
# #endif
# #ifdef _DLL_Provider
# #define _DLLAPI  _declspec(dllexport)
# #else
# #define _DLLAPI  _declspec(dllimport)
# #endif
# #ifndef EXTERNC
# #define EXTERNC   extern "C"
# #endif
# //初始化并加载音圈控制端，motor_num == 音圈电机数量（音圈电机 id=1~15）
# //不需要帮用户回零位
C_SoftLanding_dll.Soft_landing_dll_init.restype = None
C_SoftLanding_dll.Soft_landing_dll_init.argtype = [c_int]
# //设置电机运动正方向 direct == 0 正向 direct == 1反向
C_SoftLanding_dll.SetRunDirect.restype = None
C_SoftLanding_dll.SetRunDirect.argtype = [c_int, c_int]
# //手动分配电机资源
C_SoftLanding_dll.VCMT_resource_alloc.restype = None
C_SoftLanding_dll.VCMT_resource_alloc.argtype = [POINTER(VCM_Resource_struct), c_int]
# //获取音圈电机初始化状态，成功返回1，忙返回0,电机不存在返回 -1。
C_SoftLanding_dll.Get_Init_Ready.restype = c_int
C_SoftLanding_dll.Get_Init_Ready.argtype = [None]
# //显示调试窗体,卡死并等待调试窗体返回
C_SoftLanding_dll.ShowSettingDlg.restype = None
C_SoftLanding_dll.ShowSettingDlg.argtype = [None]
# //释放音圈控制端
C_SoftLanding_dll.Soft_landing_dll_uninit.restype = None
C_SoftLanding_dll.Soft_landing_dll_uninit.argtype = [None]
# //进行软着陆运动(motor_id = 音圈电机id 1~15)
# //成功返回0 失败返回起点不一致计数器
C_SoftLanding_dll.Do_Softlanding.restype = c_int
C_SoftLanding_dll.Do_Softlanding.argtype = [c_int]
# //使用指定的轨迹槽slot =0~9(10轨迹槽)
# //默认使用0号槽
# //用于快速切换轨迹槽,不需要重新计算插补参数。
C_SoftLanding_dll.SetSoftlandingSlot.restype = None
C_SoftLanding_dll.SetSoftlandingSlot.argtype = [c_int, c_int]
# //进行软着陆运动(motor_id = 音圈电机id 1~15)
# //成功返回0 失败返回起点不一致计数器
C_SoftLanding_dll.Do_SoftDown.restype = c_int
C_SoftLanding_dll.Do_SoftDown.argtype = [c_int]
# //进行软着陆运动回位(motor_id = 音圈电机id 1~15)
# //成功返回0 失败返回起点不一致计数器
C_SoftLanding_dll.Do_SoftUp.restype = c_int
C_SoftLanding_dll.Do_SoftUp.argtype = [c_int]
# //获取电机软着陆运动状态(motor_id = 音圈电机id 1~15)
# //flag_index代码 busy_flag_down == 0 busy_flag_up == 1
# //忙返回1 空闲返回0 电机不存在返回 -1
# //用于软着陆模式
C_SoftLanding_dll.Get_Busy.restype = c_int
C_SoftLanding_dll.Get_Busy.argtype = [c_int, c_int]
# //获取错误码
# //  error_over_current 1
# //  error_go_zero (1<<1)
# //  error_over_temp (1<<2)
# //  error_leakage_current (1<<3)
# //控制器错误返回-1
# //处理方法同GetControllerError
C_SoftLanding_dll.get_motor_error.restype = c_int64
C_SoftLanding_dll.get_motor_error.argtype = [c_int]
# //回零位
# //回零成功返回1 失败返回0 超时返回-1
# //需要返回错误（类型）
# //阻塞成功或者失败后返回
C_SoftLanding_dll.Init_Go_Zero.restype = c_int
C_SoftLanding_dll.Init_Go_Zero.argtype = [c_int]
# //获取当前原点开关信号
C_SoftLanding_dll.GetZeroIO.restype = c_int
C_SoftLanding_dll.GetZeroIO.argtype = [c_int]
# //设定零位偏移
C_SoftLanding_dll.SetZeroPos.restype = None
C_SoftLanding_dll.SetZeroPos.argtype = [c_int, c_double]
# //位置控制模式的运动函数
# //设置位置模式限位
# //成功返回1 失败返回0
C_SoftLanding_dll.SetPosLimit.restype = c_int
C_SoftLanding_dll.SetPosLimit.argtype = [c_int, c_double, c_double]
# //设置位置模式加加速度
# //成功返回1 失败返回0
C_SoftLanding_dll.SetPosModejerk.restype = c_int
C_SoftLanding_dll.SetPosModejerk.argtype = [c_int, c_double]
# //设置位置模式加速度
# //成功返回1 失败返回0
C_SoftLanding_dll.SetPosModeAcc.restype = c_int
C_SoftLanding_dll.SetPosModeAcc.argtype = [c_int, c_double]
# //设置位置模式速度
# //成功返回1 失败返回0
C_SoftLanding_dll.SetPosModeSpeed.restype = c_int
C_SoftLanding_dll.SetPosModeSpeed.argtype = [c_int, c_double]
# //设置目标并运动到指定位置
# //成功返回1 失败返回0
C_SoftLanding_dll.SetPosModePos.restype = c_int
C_SoftLanding_dll.SetPosModePos.argtype = [c_int, c_double]
# //等待运动停止
# //成功返回1 失败返回0
# //wait_user == 1 用户程序等待 wait_user == 0 内部指令等待
C_SoftLanding_dll.TillPosModePos.restype = c_int
C_SoftLanding_dll.TillPosModePos.argtype = [c_int, c_int]
# //获取指令缓冲长度
C_SoftLanding_dll.GetInsBuffLen.restype = c_int
C_SoftLanding_dll.GetInsBuffLen.argtype = [c_int]
# //增量运动
C_SoftLanding_dll.SGO_INCREASE.restype = None
C_SoftLanding_dll.SGO_INCREASE.argtype = [c_int, c_double]
# //插入延迟指令
C_SoftLanding_dll.AddMotorDelay.restype = None
C_SoftLanding_dll.AddMotorDelay.argtype = [c_int, c_double]
# //获取当前磁栅尺真实位置，成功返回1。
# //成功返回1 失败返回0
C_SoftLanding_dll.GetNowPos.restype = c_int
C_SoftLanding_dll.GetNowPos.argtype = [c_int, c_double]
# //获取控制器输出位置，成功返回1。
# //成功返回1 失败返回0
C_SoftLanding_dll.GetTargetPos.restype = c_int
C_SoftLanding_dll.GetTargetPos.argtype = [c_int, c_double]
# //获取到位信号 到位返回1 运动中返回0
# //用于位置模式
C_SoftLanding_dll.CheckPosReady.restype = c_int
C_SoftLanding_dll.CheckPosReady.argtype = [c_int]
# //设定最大最小电流限制（推电流MaxI<=10A,拉电流MinI>=-10A）
C_SoftLanding_dll.SetCurrentLimit.restype = c_int
C_SoftLanding_dll.SetCurrentLimit.argtype = [c_int, c_double, c_double]
C_SoftLanding_dll.SetDelay.restype = c_int
C_SoftLanding_dll.SetDelay.argtype = [c_int, c_int]
# //软着陆函数
# //设定快速进给速度
C_SoftLanding_dll.SetFastSpeed.restype = None
C_SoftLanding_dll.SetFastSpeed.argtype = [c_int, c_double]
# //设定快速进给加速度
C_SoftLanding_dll.SetFastAcc.restype = None
C_SoftLanding_dll.SetFastAcc.argtype = [c_int, c_double]
# //设定慢速接近速度
C_SoftLanding_dll.SetSlowSpeed.restype = None
C_SoftLanding_dll.SetSlowSpeed.argtype = [c_int, c_double]
# //设定慢速接近加速度
C_SoftLanding_dll.SetSlowAcc.restype = None
C_SoftLanding_dll.SetSlowAcc.argtype = [c_int, c_double]
# //设定软着陆力
C_SoftLanding_dll.SetForce.restype = None
C_SoftLanding_dll.SetForce.argtype = [c_int, c_double]
# //设定软着陆位置
C_SoftLanding_dll.SetSoftPos.restype = None
C_SoftLanding_dll.SetSoftPos.argtype = [c_int, c_double]
# //设定软着陆余量
C_SoftLanding_dll.SetSoftLandingMargin.restype = None
C_SoftLanding_dll.SetSoftLandingMargin.argtype = [c_int, c_double]
# //获取当前轨迹槽的然着陆运动时间
C_SoftLanding_dll.GetSoftlandingTime.restype = c_double
C_SoftLanding_dll.GetSoftlandingTime.argtype = [c_int]
# //更新软着陆参数至当前轨迹槽
C_SoftLanding_dll.UpdataParam.restype = None
C_SoftLanding_dll.UpdataParam.argtype = [c_int]
# //返回设定软着陆位置s，单位mm,(motor_id = 音圈电机id 1~15)
# //返回位置
# //bug待修正
C_SoftLanding_dll.Get_Softlanding_endpos.restype = c_double
C_SoftLanding_dll.Get_Softlanding_endpos.argtype = [c_int]
# //获取控制服务端错误码 ==1 则需要析构后重构
# //检测控制卡服务端状态
C_SoftLanding_dll.GetControllerError.restype = c_int
C_SoftLanding_dll.GetControllerError.argtype = [None]
# //减速急停
C_SoftLanding_dll.StopVmc.restype = None
C_SoftLanding_dll.StopVmc.argtype = [c_int]
# //计算并生成电流和力的映射表（自动插值,需要len>3）
# //m_Current电流（单位A）  m_Force力（单位g）
C_SoftLanding_dll.MapCurrent2Force.restype = None
C_SoftLanding_dll.MapCurrent2Force.argtype = [c_int, c_double, c_double, c_int]

