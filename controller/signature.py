from importlib.resources import files
from pathlib import Path
from ctypes import CDLL, c_int32, c_double, c_wchar_p

def load_dll():
    if __package__ :
        _dll_path = files(__package__).joinpath("bin", "BAiOS.dll")
    else:
        _base_dir = Path(__file__).parent
        _dll_path = _base_dir.joinpath("bin", "BAiOS.dll")

    # uc-7660.infがインストール済 ＆ 初回は実際に接続された状態でないとエラーが出る
    _dll = CDLL(str(_dll_path))

    # ┌────────────────────────── Devices ─────────────────────────────┐

    _dll.FuncDeviceOpen.argtypes = []
    _dll.FuncDeviceOpen.restype = c_int32

    _dll.FuncDeviceClose.argtypes = []
    _dll.FuncDeviceClose.restype = None

    # └────────────────────────────────────────────────────────────────┘

    # ┌──────────────────────────── IO ────────────────────────────────┐

    _dll.FuncIsORG.argtypes = [c_int32]
    _dll.FuncIsORG.restype = c_int32

    _dll.FuncIsSyringeORG.argtypes = []
    _dll.FuncIsSyringeORG.restype = c_int32

    _dll.CheckIODownSensor.argtypes = []
    _dll.CheckIODownSensor.restype = c_int32

    _dll.CheckIOPressSensor.argtypes = []
    _dll.CheckIOPressSensor.restype = c_int32

    _dll.CheckIOPressSensorPower.argtypes = []
    _dll.CheckIOPressSensorPower.restype = c_int32

    _dll.SensorPowerOnOff.argtypes = [c_int32]
    _dll.SensorPowerOnOff.restype = c_int32

    _dll.SensorZero.argtypes = []
    _dll.SensorZero.restype = c_int32

    _dll.SetThresholdNo.argtypes = [c_int32]
    _dll.SetThresholdNo.restype = c_int32

    # └────────────────────────────────────────────────────────────────┘

    # ┌─────────────────────────── Status  ────────────────────────────┐

    _dll.GetAlarmMessage.argtypes = [c_int32]
    _dll.GetAlarmMessage.restype = c_wchar_p

    _dll.FuncGetSystemCmdState.argtypes = [c_int32]
    _dll.FuncGetSystemCmdState.restype = c_int32

    _dll.FuncGetOtherCmdState.argtypes = [c_int32]
    _dll.FuncGetOtherCmdState.restype = c_int32

    _dll.FuncGetAxisState.argtypes = [c_int32, c_int32]
    _dll.FuncGetAxisState.restype = c_int32

    _dll.FuncGetState.argtypes = [c_int32]
    _dll.FuncGetState.restype = c_int32

    # └────────────────────────────────────────────────────────────────┘

    # ┌─────────────────────────── System ─────────────────────────────┐

    _dll.FuncStop.argtypes = [c_int32]
    _dll.FuncStop.restype = c_int32

    _dll.FuncContinue.argtypes = [c_int32]
    _dll.FuncContinue.restype = c_int32

    _dll.FuncEnd.argtypes = [c_int32]
    _dll.FuncEnd.restype = c_int32

    # └────────────────────────────────────────────────────────────────┘

    # ┌─────────────────────────── Axis ───────────────────────────────┐

    _dll.GetAxisPos.argtypes = [c_int32, c_int32]
    _dll.GetAxisPos.restype = c_double

    _dll.GetAxisStepPos.argtypes = [c_int32, c_int32]
    _dll.GetAxisStepPos.restype = c_int32

    _dll.FuncOrgn.argtypes = [c_int32, c_int32]
    _dll.FuncOrgn.restype = c_int32

    _dll.FuncAbsMove.argtypes = [c_int32, c_int32, c_double, c_double, c_int32]
    _dll.FuncAbsMove.restype = c_int32

    _dll.FuncAddMove.argtypes = [c_int32, c_int32, c_double, c_double, c_int32]
    _dll.FuncAddMove.restype = c_int32

    _dll.FuncSyringeAbsMove.argtypes = [c_int32, c_int32]
    _dll.FuncSyringeAbsMove.restype = c_int32

    _dll.FuncSyringeAddMove.argtypes = [c_int32, c_int32]
    _dll.FuncSyringeAddMove.restype = c_int32

    # └────────────────────────────────────────────────────────────────┘

    # ┌───────────────────────── Composite ────────────────────────────┐

    _dll.FuncXYZOrgn.argtypes = [c_int32]
    _dll.FuncXYZOrgn.restype = c_int32

    _dll.FuncPipetting.argtypes = [c_int32, c_int32, c_int32]
    _dll.FuncPipetting.restype = c_int32

    _dll.FuncLiquidLevelCheck.argtypes = [c_double, c_double, c_double, c_int32]
    _dll.FuncLiquidLevelCheck.restype = c_int32

    _dll.FuncGetLiquidLevel.argtypes = []
    _dll.FuncGetLiquidLevel.restype = c_double

    _dll.FuncTipIn.argtypes = [c_double, c_double, c_int32]
    _dll.FuncTipIn.restype = c_int32

    _dll.FuncTipOut.argtypes = [c_double, c_double, c_int32]
    _dll.FuncTipOut.restype = c_int32

    _dll.FuncXY_Move.argtypes = [c_double, c_double, c_double, c_double, c_int32]
    _dll.FuncXY_Move.restype = c_int32

    # └────────────────────────────────────────────────────────────────┘

    return _dll