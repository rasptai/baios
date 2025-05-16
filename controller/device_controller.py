from device import Device, HardID
from signature import hardware_lib

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
        self.slx = Device(HardID.SLX)
        self.img = Device(HardID.IMG)
        self._initialized = True

    def __enter__(self):
        if not self._context_count:
            self.FuncDeviceOpen()
            self.slx.start_monitor()
            self.img.start_monitor()
            print("Devices are opened and started.")

        self._context_count += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._context_count -= 1
        if not self._context_count:
            self.slx.stop_monitor()
            self.img.stop_monitor()
            self.FuncDeviceClose()
            print("Devices are stopped and closed.")

        return False

    def FuncDeviceOpen(self):
        result = hardware_lib.FuncDeviceOpen()
        if result != 0:
            raise Exception(f"Failed to open device. Error code: {result}")

    def FuncDeviceClose(self):
        hardware_lib.FuncDeviceClose()