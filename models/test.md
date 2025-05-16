:::mermaid
classDiagram
    %% Superclass representing the entire device
    class DeviceController {
        +slxDevice: SLXDevice
        +imgDevice: IMGDevice
        +openDevice(): void
        +closeDevice(): void
        +getSLX(): SLXDevice
        +getIMG(): IMGDevice
    }

    %% Abstract base for SLX and IMG devices
    class BaseDevice {
        <<abstract>>
        +hard: int
        +state: DeviceState
        +monitor: Monitor
        +positionMM: Map<Axis, double>
        +positionStep: Map<Axis, long>
        +startMonitor(): void
        +stopMonitor(): void
        +getAxisPos(axis: Axis): double
        +getAxisStepPos(axis: Axis): long
        #onStateChange(newState: DeviceState): void
    }

    %% SLX-specific device extending BaseDevice
    class SLXDevice {
        +funcTipIn(x: double, y: double, checkSensor: bool): void
        +funcTipOut(x: double, y: double, trashbox: bool): void
        +funcLiquidLevelCheck(startPos: double, endPos: double, upPos: double, threshold: int): void
        +funcPipetting(count: int, volume: int, speed: int): void
    }

    %% IMG-specific device extending BaseDevice
    class IMGDevice {
        +funcAcquire(conditionName: string, well: string): Image
        +funcMagnetStageMove(position: MagnetPosition): void
    }

    %% Monitor class for device state polling
    class Monitor {
        +hard: int
        +intervalMs: long
        +callback(state: DeviceState): void
        -stopEvent: Event
        -thread: Thread
        +start(): void
        +stop(): void
        -run(): void
    }

    %% Enumeration for axes
    class Axis {
        <<enumeration>>
        X
        Y
        Z
        P
    }

    %% Enumeration for device states
    class DeviceState {
        <<enumeration>>
        READY
        SYSTEM_BUSY
        BUSY
        STOPPED
        COLLISION_HANDLING
        COLLIDED
    }

    %% Relationships
    DeviceController *-- SLXDevice : "owns"
    DeviceController *-- IMGDevice : "owns"
    SLXDevice --|> BaseDevice
    IMGDevice --|> BaseDevice
    BaseDevice o-- Monitor : "uses"
