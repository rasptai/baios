import sys
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QColor

class WellWidget(QFrame):
    def __init__(self, size: int):
        super().__init__()
        self.size = size
        self.is_selected = False
        self.setFixedSize(size, size)
        radius = size // 2
        self._default = f"background: white; border-radius: {radius}px;"
        self._hover   = f"background: lightblue; border-radius: {radius}px;"
        self._select  = f"background: blue; border-radius: {radius}px;"
        self.setStyleSheet(self._default)
        # 子はマウスイベントを透過させる
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        # ドロップシャドウ効果
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(shadow)

    def setHighlight(self, on: bool):
        if not self.is_selected:
            self.setStyleSheet(self._hover if on else self._default)

    def setSelected(self, on: bool):
        self.is_selected = on
        self.setStyleSheet(self._select if on else self._default)


class PlateWidget(QWidget):
    def __init__(self,
                rows: int = 8,
                cols: int = 12,
                well_size: int = 50,
                spacing: int = 4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.well_size = well_size
        self.spacing = spacing

        # 前回ホバーしていたブロックの起点 (r0,c0)
        self._prev_hover = None

        # マウストラッキングで常にマウス移動を検出
        self.setMouseTracking(True)

        layout = QGridLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(spacing)

        # ウェルを二次元リストで保持
        self._wells = [[None] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                w = WellWidget(well_size)
                layout.addWidget(w, r, c)
                self._wells[r][c] = w

        self.setLayout(layout)

    def _block_at_pos(self, pos: QPoint):
        """
        マウス位置 pos から、
        どの 2×2 ブロック (r0,c0) に属するかを判定。
        ブロックはウェル中心間の矩形領域。
        """
        # 中心座標を計算（行方向と列方向で独立に取得）
        centers_x = [self._wells[0][c].geometry().center().x() for c in range(self.cols)]
        centers_y = [self._wells[r][0].geometry().center().y() for r in range(self.rows)]

        # 各 2×2 ブロックをチェック
        for r0 in range(self.rows - 1):
            y0, y1 = centers_y[r0], centers_y[r0 + 1]
            min_y, max_y = min(y0, y1), max(y0, y1)
            if not (min_y <= pos.y() <= max_y):
                continue
            for c0 in range(self.cols - 1):
                x0, x1 = centers_x[c0], centers_x[c0 + 1]
                min_x, max_x = min(x0, x1), max(x0, x1)
                if min_x <= pos.x() <= max_x:
                    return r0, c0
        return None

    def mouseMoveEvent(self, event):
        pos = event.pos()
        hit = self._block_at_pos(pos)

        # 前回と違うブロックなら切り替え
        if hit != self._prev_hover:
            # 以前のブロックをクリア
            if self._prev_hover is not None:
                pr, pc = self._prev_hover
                for dr in (0, 1):
                    for dc in (0, 1):
                        self._wells[pr + dr][pc + dc].setHighlight(False)
            # 新しいブロックをハイライト
            if hit is not None:
                r0, c0 = hit
                for dr in (0, 1):
                    for dc in (0, 1):
                        self._wells[r0 + dr][c0 + dc].setHighlight(True)
            self._prev_hover = hit

        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        pos = event.pos()
        hit = self._block_at_pos(pos)

        # クリック時はすべての選択をリセットしてから
        for r in range(self.rows):
            for c in range(self.cols):
                self._wells[r][c].setSelected(False)

        # ヒットしたブロックだけ選択色に
        if hit is not None:
            r0, c0 = hit
            for dr in (0, 1):
                for dc in (0, 1):
                    self._wells[r0 + dr][c0 + dc].setSelected(True)

        super().mousePressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    plate = PlateWidget(rows=8, cols=12, well_size=50, spacing=5)
    plate.setWindowTitle("96-Well Plate — Center-Based 2×2 Group Highlight")
    plate.show()
    sys.exit(app.exec())
