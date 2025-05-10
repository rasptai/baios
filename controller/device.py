from enum import IntEnum
import threading
import controller.signature as signature

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
            print(f"Device {self.hard} is in normal state.")
        elif state == 1:
            print(f"Device {self.hard} is in error state.")
        else:
            print(f"Device {self.hard} is in unknown state.")

    def start_monitor(self):
        self.monitor.start()

    def stop_monitor(self):
        self.monitor.stop()