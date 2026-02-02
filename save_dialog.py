import json
import os

from PySide6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QCheckBox


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
        checkboxes = []
        # Access the parent MainWindow's checkbox_layout
        for i in range(self.parent().checkbox_layout.count()):
            item = self.parent().checkbox_layout.itemAt(i)
            widget = item.widget()
            if isinstance(widget, QCheckBox):
                checkboxes.append(widget.text())

        # Create a saves directory if it doesn't exist
        os.makedirs("saves", exist_ok=True)

        checklists = {self.save_file_line_edit.text(): checkboxes}
        with open("saves/" + self.save_file_line_edit.text() + ".json", "w") as f:
            json.dump(checklists, f, indent=4)

        self.close()

    def cancel(self):
        self.close()