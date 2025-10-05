from PySide6 import QtWidgets

class AddCheckboxDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddCheckboxDialog, self).__init__(parent)
        self.setWindowTitle("Add Checkbox")
        self.setModal(True)