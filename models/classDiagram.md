::: mermaid

classDiagram

%% class BAiOS
%% class Device
%% class Stage
%% class Monitor
%% class Labware
%% class Led
  BAiOSSystem "1" *-- "1" DeviceController : uses
    BAiOSSystem "1" *-- "2" Device : has
    BAiOSSystem "1" *-- "4" Stage : has
    BAiOSSystem "1" *-- "1" LabwareFactory : uses

    DeviceController <|-- DeviceMonitor : delegates
    DeviceController "1" o-- "*" Device : provides
    Device "1" o-- "1" DeviceMonitor : has

    Stage "1" o-- "*" Labware : holds



    %% class DeviceController {
    %%     +dispense(x,y,z,vol)
    %%     +move_stage(axis, pos)
    %%     +open(), close()
    %% }
    %% class StageManager {
    %%     +place_labware(stage_id, labware)
    %%     +remove_labware(stage_id)
    %%     +get_labware(stage_id)
    %% }
    %% class SystemFacade {
    %%     +with_system(): context
    %%     +dispense_on(stage_id, well, vol)
    %%     +capture_image(stage_id)
    %% }

    %% SystemFacade --> DeviceController : uses
    %% SystemFacade --> StageManager      : uses
