from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

import re
from zxcvbn import zxcvbn

with open('/home/arka/Github/Python_PassCheck/Wordlist/MESCollege.txt') as f:
    lines = f.read().splitlines()
    passwords = []
    for line in lines:
        # split line based on spaces and commas using regular expression
        split_line = re.split(r'[ ,]+', line)
        passwords += split_line


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PassCheck")
        self.pushButton.clicked.connect(self.check_pass)

    def check_pass(self):
        name = self.UserNameInput.text().split()
        print(self.PassInput.text())
        result = zxcvbn(self.PassInput.text(), user_inputs=name+passwords)
        self.score.setText(str(result['score']))
        self.guesses.setText(str(result['guesses']))
        self.tenH.setText(str(result['crack_times_display']['online_throttling_100_per_hour']))
        self.tenKS.setText(str(result['crack_times_display']['offline_slow_hashing_1e4_per_second']))
        self.tenBS.setText(str(result['crack_times_display']['offline_fast_hashing_1e10_per_second']))
