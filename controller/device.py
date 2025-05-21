from enum import IntEnum
from monitor import Monitor
from controller_api import *

class HardID(IntEnum):
    LIQUID_HANDLER = 90010
    IMAGING_UNIT = 90050

class LiquidHandlerAxis(IntEnum):
    X = 0
    Y = 1
    Z = 2
    SYRINGE = 3

class ImagingUnitAxis(IntEnum):
    X = 0
    Y = 1
    CAMERA = 2
    MAGNET = 3

class BaseDevice:
    def __init__(self, hard: HardID):
        self.hard = hard
        self.monitor = Monitor(hard, self._on_state)
        self.position      = [0, 0, 0, 0]
        self.position_step = [0, 0, 0, 0]

    def _on_state(self, state):
        if state == 0:
            print(f"{self.hard} is Ready.")
        elif state == 1:
            print(f"{self.hard} is System Busy.")
        elif state == 2:
            print(f"{self.hard} is Busy.")
        elif state == 3:
            print(f"{self.hard} is Stop.")
        elif state == 4:
            print(f"{self.hard} is Collision Detected.")
        elif state == 5:
            print(f"{self.hard} is Stopped due to collision.")

    def start_monitor(self):
        self.monitor.start()

    def stop_monitor(self):
        self.monitor.stop()
class LiquidHandler(BaseDevice):
    def __init__(self):
        super().__init__(HardID.LIQUID_HANDLER)

    def is_syringe_homed(self):
        return is_syringe_org()

    def is_collision_sensor(self):
        return is_collision_sensor()

    def syringe_move_abs(self, speed: float, volume: float):
        return syringe_move_abs(speed, volume)
class ImagingUnit(BaseDevice):
    def __init__(self):
        super().__init__(HardID.IMAGING_UNIT)