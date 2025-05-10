from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QPushButton
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Labware Designer")
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("New Labware"))
    central = QWidget()
    central.setLayout(layout)
    window.setCentralWidget(central)
    window.show()
    sys.exit(app.exec())