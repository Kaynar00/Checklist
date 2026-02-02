from PySide6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout


class SaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Save Checklist")
        self.setFixedSize(300, 100)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.save_file_line_edit = QLineEdit()
        self.layout.addWidget(self.save_file_line_edit)

        # Make button layout
        self.button_layout = QHBoxLayout()

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.save_file)
        self.button_layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel)
        self.button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.button_layout)

    def save_file(self):
        pass

    def cancel(self):
        self.close()