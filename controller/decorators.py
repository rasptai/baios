import time
import functools
from signature import hardware_lib

def axis_command(func):
    @functools.wraps(func)
    def wrapper(self, axis, *args, **kwargs):
        result = func(self, axis, *args, **kwargs)
        if result != 0:
            return result
        while hardware_lib.FuncGetAxisState(self.hard, axis) != 0:
            time.sleep(0.01)
        return True
    return wrapper