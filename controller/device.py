from enum import IntEnum

class HardID(IntEnum):
    LIQUID_HANDLER = 90010
    IMAGING_UNIT = 90050

class LiquidHandlerAxis(IntEnum):
    X = 0
    Y = 1
    Z = 2
    SYRINGE = 3

class ImagingUnitAxis(IntEnum):
    X = 0
    Y = 1
    CAMERA = 2
    MAGNET = 3

class BaseDevice:
    def __init__(self, hard: HardID):
        self.hard = hard

class LiquidHandler(BaseDevice):
    def __init__(self):
        super().__init__(HardID.LIQUID_HANDLER)

class ImagingUnit(BaseDevice):
    def __init__(self):
        super().__init__(HardID.IMAGING_UNIT)