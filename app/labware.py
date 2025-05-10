from enum import StrEnum
from dataclasses import dataclass, field
from typing import List, Literal, Tuple

#――――――――――――――――――――
# スキーマ要素対応クラス群
#――――――――――――――――――――

class WellShape(StrEnum):
    CIRCLE    = "circle"
    RECTANGLE = "rectangle"

class Segment(StrEnum):
    SINGLE = "single"
    MULTI  = "multi"

class BottomShape(StrEnum):
    FLAT  = "flat"
    ROUND = "round"

@dataclass
class Metadata:
    name: str
    category: str
    manufacturer: str

@dataclass
class OuterDimensions:
    length: float
    width:  float
    height: float

@dataclass
class BoundingBox:
    x:      float
    y:      float
    width:  float
    height: float

@dataclass
class WellPlacement:
    count:        int
    rows:         int
    columns:      int
    well_spacing: Tuple[float, float]   # (x, y)
    a1_location:  Tuple[float, float]   # (x, y)

#――――――――――――――――――――
# ウェル断面ジオメトリ
#――――――――――――――――――――

@dataclass
class WellGeometryBase:
    shape:   WellShape
    segment: Segment

@dataclass
class CircleSingle(WellGeometryBase):
    top_offset:     float
    top_diameter:   float
    depth:          float
    bottom_diameter: float
    bottom_shape:   BottomShape

@dataclass
class CircleMulti(WellGeometryBase):
    top_offset:      float
    top_diameter:    float
    upper_depth:     float
    middle_diameter: float
    lower_depth:     float
    bottom_diameter: float
    bottom_shape:    BottomShape

@dataclass
class RectangleSingle(WellGeometryBase):
    top_offset:   float
    top_width:    float
    top_height:   float
    depth:        float
    bottom_width: float
    bottom_height: float
    bottom_shape: BottomShape

@dataclass
class RectangleMulti(WellGeometryBase):
    top_offset:    float
    top_width:     float
    top_height:    float
    upper_depth:   float
    middle_width:  float
    middle_height: float
    lower_depth:   float
    bottom_width:  float
    bottom_height: float
    bottom_shape:  BottomShape

#――――――――――――――――――――
# グループ／ラボウェア本体
#――――――――――――――――――――

@dataclass
class Group:
    bounding_box:  BoundingBox
    placement:     WellPlacement
    geometry:      WellGeometryBase

    def iter_wells(self) -> List["Well"]:
        """placement + geometry から Well インスタンスを一括生成"""
        wells: List[Well] = []
        dx, dy = self.placement.well_spacing
        ax, ay = self.placement.a1_location
        for r in range(self.placement.rows):
            for c in range(self.placement.columns):
                x = ax + c * dx
                y = ay + r * dy
                wells.append(
                    Well(row=r, column=c, x=x, y=y, geometry=self.geometry)
                )
        return wells

@dataclass
class Well:
    row:      int
    column:   int
    x:        float  # 上面投影時の X 座標
    y:        float  # 同じく Y 座標
    geometry: WellGeometryBase

@dataclass
class Labware:
    schema_version:   int
    metadata:         Metadata
    outer_dimensions: OuterDimensions
    groups:           List[Group] = field(default_factory=list)

    def all_wells(self) -> List[Well]:
        """全グループ→全ウェルをフラットに返す"""
        wells: List[Well] = []
        for g in self.groups:
            wells.extend(g.iter_wells())
        return wells