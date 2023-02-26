import hashlib
from hashgen import Ui_hash

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class hash_widget(QWidget, Ui_hash):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hash Gen")
        self.md5pushbutton.clicked.connect(self.md5gen)

    def md5gen(self):
        password = self.lineEdit.text()
        hash_oject = hashlib.md5()

        hash_oject.update(password.encode())
        hash_hex = hash_oject.hexdigest()

        self.textBrowser.setPlainText(hash_hex)


