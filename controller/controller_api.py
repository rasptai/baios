from signature import dll

def device_open() -> int:
    return dll.FuncDeviceOpen()

def device_close() -> None:
    return dll.FuncDeviceClose()

def get_alert_message(error_code: int) -> str:
    return dll.GetAlarmMessage(error_code)

def is_org(hard: int) -> int:
    return dll.FuncIsORG(hard)

def is_syringe_org() -> int:
    return dll.FuncIsSyringeORG()

def get_system_state(hard: int) -> int:
    return dll.FuncGetSystemCmdState(hard)

def get_composite_state(hard: int) -> int:
    return dll.FuncGetOtherCmdState(hard)

def get_axis_state(hard: int, axis: int) -> int:
    return dll.FuncGetAxisState(hard, axis)

def get_device_state(hard: int) -> int:
    return dll.FuncGetState(hard)

def get_axis_pos(hard: int, axis: int) -> int:
    return dll.GetAxisPos(hard, axis)

def get_axis_step_pos(hard: int, axis: int) -> int:
    return dll.GetAxisStepPos(hard, axis)

def is_collision_sensor() -> int:
    return dll.CheckIODownSensor()

def device_origin(hard: int) -> int:
    return dll.FuncXYZOrgn(hard)

def axis_origin(hard: int, axis: int) -> int:
    return dll.FuncOrgn(hard, axis)

def move_abs(hard: int, axis: int, speed: float, pos: float, collision: int) -> int:
    return dll.FuncAbsMove(hard, axis, speed, pos, collision)

def move_add(hard: int, axis: int, speed: float, pos: float, collision: int) -> int:
    return dll.FuncAddMove(hard, axis, speed, pos, collision)

def syringe_move_abs(speed: float, volume: float) -> int:
    volume = int(volume * 41.58)
    speed = int(speed * 41.58)
    return dll.FuncSyringeAbsMove(speed, volume)

def syringe_move_add(speed: float, volume: float) -> int:
    volume = int(volume * 41.58)
    speed = int(speed * 41.58)
    return dll.FuncSyringeAddMove(speed, volume)

def pipetting(count: int, volume: int, speed: int) -> int:
    volume = int(volume * 41.58)
    speed = int(speed * 41.58)
    return dll.FuncPipetting(count, volume, speed)

def liquid_level_check(start_height: float, end_height: float, elevate_height: float, threshold: int) -> int:
    return dll.FuncLiquidLevelCheck(start_height, end_height, elevate_height, threshold)

def get_liquid_level() -> float:
    return dll.FuncGetLiquidLevel()

def tip_insert(head_x: float, head_y: float, confirm: int) -> int:
    return dll.FuncTipIn(head_x, head_y, confirm)

def tip_eject(head_x: float, head_y: float, mode: int) -> int:
    return dll.FuncTipOut(head_x, head_y, mode)

def move_xy(head_x: float, head_y: float, speed_x: float, speed_y: float, z_pre_raise: int) -> int:
    return dll.FuncXY_Move(head_x, head_y, speed_x, speed_y, z_pre_raise)