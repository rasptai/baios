class BAiOS:
    _instance = None
    _initialized = False
    _context_count = 0 # with文で呼び出されている回数をカウント

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
            self.slx.start_poll()
            self.img.start_poll()
            print("Devices are opened and started.")

        self._context_count += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._context_count -= 1
        if not self._context_count:
            self.slx.stop_poll()
            self.img.stop_poll()
            self.FuncDeviceClose()
            print("Devices are stopped and closed.")

        return False

    def FuncDeviceOpen(self):
        result = signature.hardware_lib.FuncDeviceOpen()
        if result != 0:
            raise Exception(f"Failed to open device. Error code: {result}")

    def FuncDeviceClose(self):
        signature.hardware_lib.FuncDeviceClose()