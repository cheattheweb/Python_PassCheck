from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
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
        result = zxcvbn(self.PassInput.text(), user_inputs=name + passwords)
        self.score.setText(str(result['score']))
        self.guesses.setText(str(result['guesses']))
        self.tenH.setText(str(result['crack_times_display']['online_throttling_100_per_hour']))
        self.tenKS.setText(str(result['crack_times_display']['offline_slow_hashing_1e4_per_second']))
        self.tenBS.setText(str(result['crack_times_display']['offline_fast_hashing_1e10_per_second']))

        #li = ['matched_word', 'rank', 'pattern', 'reversed', 'guesses', 'dictionary_name']
        li = ['l33t','uppercase_variations','i','l33t_variations','base_guesses', 'guesses_log10','j']
        result_str = ""
        for key, value in result.items():
            if key == 'sequence':
                for value2 in value:
                    for key2, value3 in value2.items():
                        if key2 not in li:
                            result_str += f"{key2}: {value3}\n"
                    result_str += "-------------------------\n\n"

        self.textBrowser.setPlainText(result_str)
