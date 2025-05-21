from importlib.resources import files
from pathlib import Path
from ctypes import CDLL, c_int32, c_double, c_char_p

if __package__ :
    dll_path = files(__package__).joinpath("bin", "BAiOS.dll")
else:
    base_dir = Path(__file__).parent
    dll_path = base_dir.joinpath("bin", "BAiOS.dll")

# uc-7660.infがインストール済 ＆ 初回は実際に接続された状態でないとエラーが出る
dll = CDLL(str(dll_path))

# ┌────────────────────────── Devices ─────────────────────────────┐

dll.FuncDeviceOpen.argtypes = []
dll.FuncDeviceOpen.restype = c_int32

dll.FuncDeviceClose.argtypes = []
dll.FuncDeviceClose.restype = None

# └────────────────────────────────────────────────────────────────┘

# ┌──────────────────────────── IO ────────────────────────────────┐

dll.FuncIsORG.argtypes = [c_int32]
dll.FuncIsORG.restype = c_int32

dll.FuncIsSyringeORG.argtypes = []
dll.FuncIsSyringeORG.restype = c_int32

dll.CheckIODownSensor.argtypes = []
dll.CheckIODownSensor.restype = c_int32

dll.CheckIOPressSensor.argtypes = []
dll.CheckIOPressSensor.restype = c_int32

dll.CheckIOPressSensorPower.argtypes = []
dll.CheckIOPressSensorPower.restype = c_int32

dll.SensorPowerOnOff.argtypes = [c_int32]
dll.SensorPowerOnOff.restype = c_int32

dll.SensorZero.argtypes = []
dll.SensorZero.restype = c_int32

dll.SetThresholdNo.argtypes = [c_int32]
dll.SetThresholdNo.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌─────────────────────────── Status  ────────────────────────────┐

dll.GetAlarmMessage.argtypes = [c_int32]
dll.GetAlarmMessage.restype = c_char_p

dll.FuncGetSystemCmdState.argtypes = [c_int32]
dll.FuncGetSystemCmdState.restype = c_int32

dll.FuncGetOtherCmdState.argtypes = [c_int32]
dll.FuncGetOtherCmdState.restype = c_int32

dll.FuncGetAxisState.argtypes = [c_int32, c_int32]
dll.FuncGetAxisState.restype = c_int32

dll.FuncGetState.argtypes = [c_int32]
dll.FuncGetState.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌─────────────────────────── System ─────────────────────────────┐

dll.FuncStop.argtypes = [c_int32]
dll.FuncStop.restype = c_int32

dll.FuncContinue.argtypes = [c_int32]
dll.FuncContinue.restype = c_int32

dll.FuncEnd.argtypes = [c_int32]
dll.FuncEnd.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌─────────────────────────── Axis ───────────────────────────────┐

dll.GetAxisPos.argtypes = [c_int32, c_int32]
dll.GetAxisPos.restype = c_double

dll.GetAxisStepPos.argtypes = [c_int32, c_int32]
dll.GetAxisStepPos.restype = c_int32

dll.FuncOrgn.argtypes = [c_int32, c_int32]
dll.FuncOrgn.restype = c_int32

dll.FuncAbsMove.argtypes = [c_int32, c_int32, c_double, c_double, c_int32]
dll.FuncAbsMove.restype = c_int32

dll.FuncAddMove.argtypes = [c_int32, c_int32, c_double, c_double, c_int32]
dll.FuncAddMove.restype = c_int32

dll.FuncSyringeAbsMove.argtypes = [c_int32, c_int32]
dll.FuncSyringeAbsMove.restype = c_int32

dll.FuncSyringeAddMove.argtypes = [c_int32, c_int32]
dll.FuncSyringeAddMove.restype = c_int32

# └────────────────────────────────────────────────────────────────┘

# ┌───────────────────────── Composite ────────────────────────────┐

dll.FuncXYZOrgn.argtypes = [c_int32]
dll.FuncXYZOrgn.restype = c_int32

dll.FuncPipetting.argtypes = [c_int32, c_int32, c_int32]
dll.FuncPipetting.restype = c_int32

dll.FuncLiquidLevelCheck.argtypes = [c_double, c_double, c_double, c_int32]
dll.FuncLiquidLevelCheck.restype = c_int32

dll.FuncGetLiquidLevel.argtypes = []
dll.FuncGetLiquidLevel.restype = c_double

dll.FuncTipIn.argtypes = [c_double, c_double, c_int32]
dll.FuncTipIn.restype = c_int32

dll.FuncTipOut.argtypes = [c_double, c_double, c_int32]
dll.FuncTipOut.restype = c_int32

dll.FuncXY_Move.argtypes = [c_double, c_double, c_double, c_double, c_int32]
dll.FuncXY_Move.restype = c_int32

# └────────────────────────────────────────────────────────────────┘
