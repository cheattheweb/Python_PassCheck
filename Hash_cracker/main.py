#!/usr/bin/env python3

import sys
from PySide6.QtWidgets import QApplication
from crack_widget import Cracker

app = QApplication(sys.argv)
window = Cracker()

window.show()
app.exec()
