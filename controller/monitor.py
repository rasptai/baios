from signature import dll
import threading
class Monitor:
    def __init__(self, hard, callback, interval=0.1):
        self.hard_id = hard
        self.callback = callback
        self.interval = interval
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        if not self._thread.is_alive():
            self._stop_event.clear()
            self._thread.start()

    def stop(self):
        self._stop_event.set()       # スレッドを停止する
        if self._thread.is_alive():
            self._thread.join()      # 停止指示を出した後、スレッドが終了するまで待機

    def _run(self):
        last_state = None
        while not self._stop_event.is_set():
            state = dll.FuncGetState(self.hard_id)
            if state != last_state:
                self.callback(state)
                last_state = state
            self._stop_event.wait(self.interval)

