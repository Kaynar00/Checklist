from PySide6.QtWidgets import QDialog


class LoadDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Load Checklist")
        self.setFixedSize(300, 100)