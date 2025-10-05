from PySide6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton


class AddCheckboxDialog(QDialog):
    def __init__(self, parent=None):
        super(AddCheckboxDialog, self).__init__(parent)
        self.setWindowTitle("Add Checkbox")
        self.setModal(True)

        self.layout = QVBoxLayout()

        # Make sure the dialog uses this layout
        self.setLayout(self.layout)

        self.label_line_edit = QLineEdit()
        self.layout.addWidget(self.label_line_edit)

        self.button_layout = QHBoxLayout()

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.button_layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.button_layout)