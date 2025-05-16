from enum import IntEnum
from signature import hardware_lib
from monitor import Monitor

class HardID(IntEnum):
    SLX = 90010
    IMG = 90050

# SLX, IMGそれぞれのデバイス単体を表すクラス
class Device:
    def __init__(self, hard: HardID):
        self.hard = hard
        self.state = None
        self.monitor = Monitor(hard, self._on_state)

    def _on_state(self, state):
        self.state = state
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
            print(f"{self.hard} is Collision Stop.")

    def start_monitor(self):
        self.monitor.start()

    def stop_monitor(self):
        self.monitor.stop()