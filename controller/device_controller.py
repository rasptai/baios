from signature import dll
class DeviceController:
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
        self._ref_count -= 1
        if not self._ref_count:
            self.device_close()
            print("Devices are stopped and closed.")
        return False

    def device_open(self):
        result = dll.FuncDeviceOpen()
        if result != 0:
            raise Exception(f"Failed to open device. Error code: {result}")

    def device_close(self):
        dll.FuncDeviceClose()

    # def is_org(self, hard):
    #     return self._dll.FuncIsOrg(hard)

    # def is_syringe_org(self):
    #     return self._dll.FuncIsSyringeOrg()

    # @system_command
    # def device_stop(self, hard):
    #     return self._dll.FuncStop(hard)

    # @system_command
    # def device_continue(self, hard):
    #     return self._dll.FuncContinue(hard)

    # @system_command
    # def device_end(self, hard):
    #     return self._dll.FuncEnd(hard)

    # def get_axis_position(self, hard, axis):
    #     return self._dll.GetAxisPos(hard, axis)

    # def get_axis_step_position(self, hard, axis):
    #     return self._dll.GetAxisStepPos(hard, axis)

    # def is_collision_sensor(self):
    #     return self._dll.CheckIODownSensor()

    # @composite_command
    # def device_origin(self, hard):
    #     return self._dll.FuncXYZOrgn(hard)

    # @axis_command
    # def axis_origin(self, hard, axis):
    #     return self._dll.FuncOrgn(hard, axis)

    # @axis_command
    # def axis_abs_move(self, hard, axis, pos, collision):
    #     return self._dll.FuncAbsMove(hard, axis, pos, collision)

    # @axis_command
    # def axis_add_move(self, hard, axis, pos, collision):
    #     return self._dll.FuncAddMove(hard, axis, pos, collision)

    # @axis_command
    # def syringe_abs_move(self, speed, volume):
    #     return self._dll.FuncSyringeAbsMove(speed, volume)

    # @axis_command
    # def syringe_add_move(self, speed, volume):
    #     return self._dll.FuncSyringeAddMove(speed, volume)

    # @composite_command
    # def pipetting(self, count, volume, speed):
    #     return self._dll.FuncPipetting(count, volume, speed)

    # @composite_command
    # def liquid_level_detection(self, start_pos, end_pos, up_pos, threshold):
    #     return self._dll.FuncLiquidLevelCheck(start_pos, end_pos, up_pos, threshold)

    # @composite_command
    # def get_liquid_level(self):
    #     return self._dll.FuncGetLiquidLevel()

    # @composite_command
    # def tip_insert(self, x_pos, y_pos, sensor):
    #     return self._dll.FuncTipIn(x_pos, y_pos, sensor)

    # @composite_command
    # def tip_eject(self, x_pos, y_pos, mode):
    #     return self._dll.FuncTipOut(x_pos, y_pos, mode)

    # @composite_command
    # def xy_move(self, x_pos, y_pos, x_speed, y_speed, before_up):
    #     return self._dll.FuncXYMove(x_pos, y_pos, x_speed, y_speed, before_up)

    # def is_pressure_sensor(self):
    #     return self._dll.CheckIOPressSensor()

    # def is_pressure_sensor(self):
    #     return self._dll.CheckIOPressSensorPower()

    # def pressure_sensor_power(self, power):
    #     return self._dll.SensorPowerOnOff(power)