import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication(sys.argv)
window = Widget()

window.setWindowTitle("PassCheck")

window.show()
app.exec()