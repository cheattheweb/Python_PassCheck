import sys
from PySide6.QtWidgets import QApplication
from widegt_hash import hash_widget

app = QApplication(sys.argv)
window = hash_widget()

window.show()
app.exec()