# ---------------------------------------
# 画面上にQFrameで装置のプレートステージ1~3を横並びで表現する
# プレートステージはANSI/SBS規格のウェルプレート・チューブラックなどが縦置きで配置できる形状なので、Width: 85.48, Height: 127.76
# 画面背景色は#f5f5f5とし、QFrameの背景色も同様だがフレーム内側でシャドウを入れることで立体感を出すこと。
# 画面上にはQHBoxLayoutで3つのQFrameを横並びに配置する。間隔は30pxとする。
# ---------------------------------------

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout

class PlateStage(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plate Stage")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #f5f5f5;")

        layout = QHBoxLayout()

        for _ in range(3):
            plate_stage = PlateStage(self)
            layout.addWidget(plate_stage)

        container = QFrame(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())