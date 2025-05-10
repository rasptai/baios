import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton,
    QGraphicsDropShadowEffect
)
from PySide6.QtCore import (
    Qt, QRect, QPropertyAnimation, QSequentialAnimationGroup,
    QEasingCurve, Slot
)
from PySide6.QtGui import QColor

class WellButton(QPushButton):
    def __init__(self, row: int, col: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col

        # トグル可能＆見た目設定
        self.setCheckable(True)
        self.setFixedSize(40, 40)
        self.setStyleSheet('''
            QPushButton {
                background-color: white;
                border: none;
                border-radius: 20px;
            }
            QPushButton:checked {
                background-color: #6cbe6c;
            }
        ''')

        # ドロップシャドウ効果
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(shadow)

        # アニメーション用グループを用意
        self.anim = QSequentialAnimationGroup(self)

class PlateWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QGridLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        for i in range(8):
            for j in range(12):
                btn = WellButton(i, j, text=f"{chr(ord('A')+i)}{j+1}")
                layout.addWidget(btn, i, j)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("モダン96ウェルプレート GUI")
        self.setCentralWidget(PlateWidget(self))
        # 少し余裕をもったサイズ
        self.resize(12*56, 8*56)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
