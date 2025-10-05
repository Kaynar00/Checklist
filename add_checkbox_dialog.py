from PySide6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton


class AddCheckboxDialog(QDialog):
    def __init__(self, parent=None):
        super(AddCheckboxDialog, self).__init__(parent)
        self.setWindowTitle("Add Checkbox")
        self.setModal(True)

        self.layout = QVBoxLayout()

        self.label_line_edit = QLineEdit()
        self.layout.addWidget(self.label_line_edit)

        # Make sure the dialog uses this layout
        self.setLayout(self.layout)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.layout.addWidget(self.cancel_button)