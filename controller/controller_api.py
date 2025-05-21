from signature import dll
import time

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

def abs_move(hard: int, axis: int, speed: float, pos: float, collision: int) -> int:
    return dll.FuncAbsMove(hard, axis, speed, pos, collision)

def add_move(hard: int, axis: int, speed: float, pos: float, collision: int) -> int:
    return dll.FuncAddMove(hard, axis, speed, pos, collision)

def syringe_abs_move(speed: float, volume: float) -> int:
    volume = int(volume * 41.58)
    speed = int(speed * 41.58)
    return dll.FuncSyringeAbsMove(speed, volume)

def syringe_add_move(speed: float, volume: float) -> int:
    volume = int(volume * 41.58)
    speed = int(speed * 41.58)
    return dll.FuncSyringeAddMove(speed, volume)

def pipetting(count: int, volume: int, speed: int) -> int:
    volume = int(volume * 41.58)
    speed = int(speed * 41.58)
    return dll.FuncPipetting(count, volume, speed)

print(device_open())
print(axis_origin(90010, 3))
time.sleep(5)
# abs_move(90010, 0, 100, 100, 0)
# time.sleep(4)
print(pipetting(2, 100, 100))
time.sleep(10)
print(syringe_abs_move(100, 100))
time.sleep(3)
print(get_axis_step_pos(90010, 3)/41.58)
# print(is_org(90010))
device_close()