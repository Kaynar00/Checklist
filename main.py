from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checklist")
        self.setGeometry(100, 100, 640, 480)

        self.layout = QVBoxLayout()

        self.checkbox_label = QLabel("Checkboxes:")
        self.layout.addWidget(self.checkbox_label)

        self.checkbox = QCheckBox("First checkbox")
        self.layout.addWidget(self.checkbox)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())