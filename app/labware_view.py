from PySide6.QtWidgets import QApplication, QWidget, QGridLayout
from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import sys

from labware import Labware, Metadata, OuterDimensions, BoundingBox, WellPlacement, RectangleSingle, Group, WellShape, Segment, BottomShape

# --- Reuse WellWidget from plate_mouse_hover.py ---
class WellWidget(QFrame):
    def __init__(self, size: int, shape: WellShape = WellShape.CIRCLE):
        super().__init__()
        # Set size
        self.setFixedSize(size, size)
        # Determine border radius based on shape
        radius = (size // 2) if shape == WellShape.CIRCLE else 0
        self._default = f"background: white; border-radius: {radius}px;"
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(8)
        shadow.setOffset(0, 2)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(shadow)
        self.setStyleSheet(self._default)

class LabwareWidget(QWidget):
    def __init__(self, labware: Labware, well_size: int = 40, spacing: int = 8, parent=None):
        super().__init__(parent)
        # Use first group for layout
        if not labware.groups:
            return
        group = labware.groups[0]
        rows = group.placement.rows
        cols = group.placement.columns

        layout = QGridLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(spacing)

        # create wells
        self._widgets = [[None] * cols for _ in range(rows)]
        for well in group.iter_wells():
            # Create widget with appropriate shape
            w = WellWidget(well_size, shape=well.geometry.shape)
            layout.addWidget(w, well.row, well.column)
            self._widgets[well.row][well.column] = w

        self.setLayout(layout)

if __name__ == "__main__":
    # Example Labware construction
    metadata = Metadata(name="Custom Plate", category="plate", manufacturer="Acme")
    outer = OuterDimensions(length=127.76, width=85.48, height=14.22)
    bbox = BoundingBox(x=0.0, y=0.0, width=127.76, height=85.48)
    placement = WellPlacement(count=96, rows=8, columns=12, well_spacing=(9.0, 9.0), a1_location=(11.0, 11.0))
    geometry = RectangleSingle(shape=WellShape.RECTANGLE, segment=Segment.SINGLE,
                             top_offset=0.0, top_width=6.7, top_height=4.7, depth=14.22,
                             bottom_width=6.7, bottom_height=6.7, bottom_shape=BottomShape.FLAT)
    group = Group(bounding_box=bbox, placement=placement, geometry=geometry)
    lab = Labware(schema_version=1, metadata=metadata, outer_dimensions=outer, groups=[group])

    app = QApplication(sys.argv)
    widget = LabwareWidget(lab, well_size=40, spacing=8)
    widget.setWindowTitle("Labware View")
    widget.show()
    sys.exit(app.exec())
