from api.controller.device_controller import DeviceController

class BAiOS():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super().__new__(cls)
            instance._ref_count = 0         # with文で呼び出されている回数をカウント
            cls._instance = instance
        return cls._instance

    def __enter__(self):
        if not self._ref_count:
            self.device_open()
            print("Devices are opened and started.")

        self._ref_count += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        