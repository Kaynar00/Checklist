from PySide6.QtWidgets import QDialog, QLineEdit, QVBoxLayout


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