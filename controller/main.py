from enum import IntEnum
import threading
import controller.signature as signature
import time

def axis_command(func):
    def wrapper(self, axis, *args, **kwargs):
        if signature.hardware_lib.FuncGetAxisState(self.hard, axis) != 0:
            return False
        result = func(self, axis, *args, **kwargs)
        if result != 0:
            return result
        while signature.hardware_lib.FuncGetAxisState(self.hard, axis) != 0:
            time.sleep(0.01)
        return True
    return wrapper

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

if __name__ == "__main__":
    with BAiOS() as baios:
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "org":
                # SLX/IMG を並列に原点復帰
                for dev in (baios.slx, baios.img):
                    threading.Thread(target=dev.xyz_orgn, daemon=True).start()
                print("→ Origin commands dispatched.")

            elif cmd == "stop":
                # 並列停止
                for dev in (baios.slx, baios.img):
                    threading.Thread(target=dev.stop, daemon=True).start()
                print("→ Stop dispatched.")
                choice = input("再開:0, 終了:1 > ").strip()
                if choice == "0":
                    for dev in (baios.slx, baios.img):
                        threading.Thread(target=dev.resume, daemon=True).start()
                    print("→ Continue dispatched.")
                elif choice == "1":
                    for dev in (baios.slx, baios.img):
                        threading.Thread(target=dev.end, daemon=True).start()
                    print("→ End dispatched. Exiting.")
                    break
                else:
                    print("⚠️ 非対応の選択肢です。")

            elif cmd.startswith("move"):
                try:
                    params = cmd.split(None, 1)[1]
                    hard, axis, speed, pos, clash = map(int, params.split(","))
                    if hard == 90010:
                        baios.slx.abs_move(axis, speed, pos, clash)
                    elif hard == 90050:
                        baios.img.abs_move(axis, speed, pos, clash)
                    else:
                        print("⚠️ 'hard' は 90010 または 90050 を指定してください。")
                except Exception:
                    print("⚠️ 'move' コマンドの引数は 'hard, axis, speed, pos, clash' の形式で指定してください。")
                    print("例: move 90010, 1, 100.0, 50.0, 0")
            elif cmd in ("exit", "quit"):
                print("Exiting CLI.")
                break

            else:
                print("⚠️ 'org' または 'stop' を入力してください。")