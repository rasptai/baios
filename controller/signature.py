from importlib.resources import files
from pathlib import Path
from ctypes import CDLL, c_int32, c_double, c_wchar_p

# ┌─────────────────── acquire the dll path ───────────────────────┐

if __package__ :
    _dll_path = files(__package__).joinpath("_hardware_driver", "BAiOS.dll")
else:
    _base_dir = Path(__file__).parent
    _dll_path = _base_dir.joinpath("_hardware_driver", "BAiOS.dll")

hardware_lib = CDLL(str(_dll_path)) # uc-7660.infがインストール済 ＆ 初回は実際に接続された状態でないとエラーが出る

# └────────────────────────────────────────────────────────────────┘

# ┌────────────────────────── Devices ─────────────────────────────┐

hardware_lib.FuncDeviceOpen.argtypes = []
hardware_lib.FuncDeviceOpen.restype = c_int32

hardware_lib.FuncDeviceClose.argtypes = []
hardware_lib.FuncDeviceClose.restype = None

# └────────────────────────────────────────────────────────────────┘

# ┌──────────────────────────── IO ────────────────────────────────┐

hardware_lib.FuncIsORG.argtypes = [c_int32]
hardware_lib.FuncIsORG.restype = c_int32

hardware_lib.FuncIsSyringeORG.argtypes = []
hardware_lib.FuncIsSyringeORG.restype = c_int32

hardware_lib.CheckIODownSensor.argtypes = []
hardware_lib.CheckIODownSensor.restype = c_int32

hardware_lib.CheckIOPressSensor.argtypes = []
hardware_lib.CheckIOPressSensor.restype = c_int32

hardware_lib.CheckIOPressSensorPower.argtypes = []
hardware_lib.CheckIOPressSensorPower.restype = c_int32

hardware_lib.SensorPowerOnOff.argtypes = [c_int32]
hardware_lib.SensorPowerOnOff.restype = c_int32

hardware_lib.SensorZero.argtypes = []
hardware_lib.SensorZero.restype = c_int32

hardware_lib.SetThresholdNo.argtypes = [c_int32]
hardware_lib.SetThresholdNo.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌─────────────────────────── Status  ────────────────────────────┐

hardware_lib.GetAlarmMessage.argtypes = [c_int32]
hardware_lib.GetAlarmMessage.restype = c_wchar_p

hardware_lib.FuncGetSystemCmdState.argtypes = [c_int32]
hardware_lib.FuncGetSystemCmdState.restype = c_int32

hardware_lib.FuncGetOtherCmdState.argtypes = [c_int32]
hardware_lib.FuncGetOtherCmdState.restype = c_int32

hardware_lib.FuncGetAxisState.argtypes = [c_int32, c_int32]
hardware_lib.FuncGetAxisState.restype = c_int32

hardware_lib.FuncGetState.argtypes = [c_int32]
hardware_lib.FuncGetState.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌─────────────────────────── System ─────────────────────────────┐

hardware_lib.FuncStop.argtypes = [c_int32]
hardware_lib.FuncStop.restype = c_int32

hardware_lib.FuncContinue.argtypes = [c_int32]
hardware_lib.FuncContinue.restype = c_int32

hardware_lib.FuncEnd.argtypes = [c_int32]
hardware_lib.FuncEnd.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌─────────────────────────── Axis ───────────────────────────────┐

hardware_lib.GetAxisPos.argtypes = [c_int32, c_int32]
hardware_lib.GetAxisPos.restype = c_double

hardware_lib.GetAxisStepPos.argtypes = [c_int32, c_int32]
hardware_lib.GetAxisStepPos.restype = c_int32

hardware_lib.FuncOrgn.argtypes = [c_int32, c_int32]
hardware_lib.FuncOrgn.restype = c_int32

hardware_lib.FuncAbsMove.argtypes = [c_int32, c_int32, c_double, c_double, c_int32]
hardware_lib.FuncAbsMove.restype = c_int32

hardware_lib.FuncAddMove.argtypes = [c_int32, c_int32, c_double, c_double, c_int32]
hardware_lib.FuncAddMove.restype = c_int32

hardware_lib.FuncSyringeAbsMove.argtypes = [c_int32, c_int32]
hardware_lib.FuncSyringeAbsMove.restype = c_int32

hardware_lib.FuncSyringeAddMove.argtypes = [c_int32, c_int32]
hardware_lib.FuncSyringeAddMove.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌───────────────────────── Composite ────────────────────────────┐

hardware_lib.FuncXYZOrgn.argtypes = [c_int32]
hardware_lib.FuncXYZOrgn.restype = c_int32

hardware_lib.FuncPipetting.argtypes = [c_int32, c_int32, c_int32]
hardware_lib.FuncPipetting.restype = c_int32

hardware_lib.FuncLiquidLevelCheck.argtypes = [c_double, c_double, c_double, c_int32]
hardware_lib.FuncLiquidLevelCheck.restype = c_int32

hardware_lib.FuncGetLiquidLevel.argtypes = []
hardware_lib.FuncGetLiquidLevel.restype = c_double

hardware_lib.FuncTipIn.argtypes = [c_double, c_double, c_int32]
hardware_lib.FuncTipIn.restype = c_int32

hardware_lib.FuncTipOut.argtypes = [c_double, c_double, c_int32]
hardware_lib.FuncTipOut.restype = c_int32

hardware_lib.FuncXY_Move.argtypes = [c_double, c_double, c_double, c_double, c_int32]
hardware_lib.FuncXY_Move.restype = c_int32

# └────────────────────────────────────────────────────────────────┘