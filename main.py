from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox, QLabel, QVBoxLayout, QWidget, QPushButton, QDialog
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

        self.add_checkbox_button = QPushButton("Add")
        self.add_checkbox_button.clicked.connect(self.add_checkbox)
        self.layout.addWidget(self.add_checkbox_button)

        self.clear_checked_boxes_button = QPushButton("Clear Checked")
        self.clear_checked_boxes_button.clicked.connect(self.clear_checked_boxes)
        self.layout.addWidget(self.clear_checked_boxes_button)

        # Push any extra vertical space to the bottom of the window
        self.layout.addStretch(1)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

    def add_checkbox(self):
        dlg = AddCheckboxDialog(self)
        dlg.exec()
        cb = QCheckBox(dlg.label_line_edit.text())
        if dlg.result() == QDialog.Accepted:
            self.checkbox_layout.addWidget(cb)

    def clear_checked_boxes(self):
        for i in reversed(range(self.checkbox_layout.count())):
            item = self.checkbox_layout.itemAt(i)
            w = item.widget()
            if isinstance(w, QCheckBox) and w.isChecked():
                self.checkbox_layout.takeAt(i)
                w.deleteLater()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())