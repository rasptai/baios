::: mermaid
classDiagram

class BAiOS

class Controller

class BaseDevice {
  +hard
  +state
  +position
  +position_step
  +monitor
  +start_monitor()
  +stop_monitor()
  +get_axis_pos()
  +get_axis_step_pos()
  -on_state()
}

class LiquidHandler

class ImagingUnit

class StatusMonitor {
  +hard
  +interval
  +callback
  -stop_event
  -thread
  +start()
  +stop()
  -run()
}

class Deck
class Stage

class Labware

BAiOS *-- "1" Controller: 合成
BAiOS *-- "1" Deck    : 合成

Controller *-- "1" LiquidHandler: 合成
Controller *-- "1" ImagingUnit  : 合成

BaseDevice <|-- LiquidHandler: 継承
BaseDevice <|-- ImagingUnit  : 継承
BaseDevice *-- StatusMonitor : 合成

Deck *-- "4" Stage: 合成
Stage o-- Labware: 集約

LiquidHandler --> Deck: 参照