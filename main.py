from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox, QLabel, QVBoxLayout, QWidget, QPushButton
from add_checkbox_dialog import AddCheckboxDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checklist")
        self.setGeometry(100, 100, 640, 480)

        self.layout = QVBoxLayout()

        self.checkbox_label = QLabel("Checkboxes:")
        self.layout.addWidget(self.checkbox_label)

        self.checkbox_layout = QVBoxLayout()
        self.layout.addLayout(self.checkbox_layout)

        self.checkbox = QCheckBox("First checkbox")
        self.checkbox_layout.addWidget(self.checkbox)

        self.add_checkbox_button = QPushButton("Add")
        self.add_checkbox_button.clicked.connect(self.add_checkbox)
        self.layout.addWidget(self.add_checkbox_button)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

    def add_checkbox(self):
        dlg = AddCheckboxDialog(self)
        dlg.exec()
        cb = QCheckBox(dlg.label_line_edit.text())
        self.checkbox_layout.addWidget(cb)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())