import time
import functools
from signature import dll

def axis_command(_func=None, *, hard=None, axis=None):
    """
    単軸命令実行前後に状態チェックを挟むデコレータ
    FuncAbsMove(hard, axis, speed, pos, collision)のようにhard, axisを引数に持つ関数はデコレータ引数が不要
    FuncSyringeAbsMove(speed, volume)のようにhard, axisを引数に持たない関数はデコレータ引数が必要
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            _hard = hard if hard is not None else args[0] # デコレータにhardが指定されていない場合はfunc引数から取得
            _axis = axis if axis is not None else args[1] # デコレータにaxisが指定されていない場合はfunc引数から取得

            state_before = dll.FuncGetAxisState(_hard, _axis)
            if state_before != 0:
                return state_before

            ret = func(self, *args, **kwargs)

            if ret != 0:
                return ret

            while dll.FuncGetAxisState(_hard, _axis) != 0:
                time.sleep(0.1)

            return ret

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)

def composite_command(_func=None, *, hard=None):
    """
    複合命令実行前後に状態チェックを挟むデコレータ
    FuncXYZOrgn(hard)のようにhardを引数に持つ関数はデコレータ引数が不要
    FuncPipetting(count, volume, speed)のようにhardを引数に持たない関数はデコレータ引数が必要
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            _hard = hard if hard is not None else args[0] # デコレータにhardが指定されていない場合はfunc引数から取得

            state_before = dll.FuncGetOtherCmdState(_hard)
            if state_before != 0:
                return state_before

            ret = func(self, *args, **kwargs)

            if ret != 0:
                return ret

            while dll.FuncGetOtherCmdState(_hard) != 0:
                time.sleep(0.1)

            return ret

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)

def system_command(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        state_before = dll.FuncGetSystemCmdState(self.hard)
        if state_before != 0:
            return state_before

        ret = func(self, *args, **kwargs)

        if ret != 0:
            return ret

        while dll.FuncGetSystemCmdState(self.hard) != 0:
            time.sleep(0.1)

        return ret

class Test:
    def __init__(self, hard):
        self.hard = hard

    @axis_command
    def test_axis_command(self, hard, axis):
        print(f"Executing axis command on hard: {hard}, axis: {axis}")
        return 0

    @composite_command
    def test_composite_command(self, hard):
        print(f"Executing composite command on hard: {hard}")
        return 0

    @system_command
    def test_system_command(self, hard):
        print(f"Executing system command on hard: {hard}")
        return 0