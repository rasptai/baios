::: mermaid

classDiagram

class DeviceController {
  +liquid_handler: SLXDevice
  +imaging_unit:   IMGDevice
}

class BaseDevice {
  +hard
  +state
  +monitor
  +position_mm: dict
  +position_step: dict
  +start_monitor()
  +stop_monitor()
  +get_axis_pos()
  +get_axis_step_pos()
  -on_state()
}

class SLXDevice

class IMGDevice

class Monitor {
  +hard
  +interval
  +callback
  -stop_event
  -thread
  +start()
  +stop()
  -run()
}

BaseDevice <|-- SLXDevice : 継承
BaseDevice <|-- IMGDevice : 継承
DeviceController "1" *-- "1" SLXDevice : has
DeviceController "1" *-- "1" IMGDevice : has
SLXDevice "1" o-- "1" Monitor : 合成
IMGDevice "1" o-- "1" Monitor : 合成