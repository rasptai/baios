# 独立したスレッドでBAiOSを監視するクラス
class Monitor:
    def __init__(self, hard, callback, interval=0.1):
        self.hard_id = hard
        self.callback = callback
        self.interval = interval
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        while not self._stop_event.is_set():
            state = signature.hardware_lib.FuncGetState(self.hard_id)
            self.callback(state)
            self._stop_event.wait(self.interval)

    def start(self):
        if not self._thread.is_alive():
            self._stop_event.clear()
            self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread.is_alive():
            self._thread.join()
