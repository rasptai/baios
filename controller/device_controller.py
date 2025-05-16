from enum import IntEnum
from monitor import Monitor
from signature import hardware_lib

class HardID(IntEnum):
    SLX = 90010
    IMG = 90050
class DeviceController:
    _instance = None
    _initialized = False
    _ref_count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.monitors = {}
        for hard in {HardID.SLX, HardID.IMG}:
            self.monitors[hard] = Monitor(hard, self._on_state)
        self._initialized = True

    def __enter__(self):
        if not self._ref_count:
            self.device_open()
            for monitor in self.monitors.values():
                monitor.start()
            print("Devices are opened and started.")

        self._ref_count += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._ref_count -= 1
        if not self._ref_count:
            for monitor in self.monitors.values():
                monitor.stop()
            self.device_close()
            print("Devices are stopped and closed.")
        return False

    def _on_state(self, hard, state):
        self.states[hard] = state
        print(f"State changed: {hard} -> {state}")

    def device_open(self):
        result = hardware_lib.FuncDeviceOpen()
        if result != 0:
            raise Exception(f"Failed to open device. Error code: {result}")

    def device_close(self):
        hardware_lib.FuncDeviceClose()