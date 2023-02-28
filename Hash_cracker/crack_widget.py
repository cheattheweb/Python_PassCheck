from PySide6.QtWidgets import QWidget
from cracker import Ui_Cracker
import hashlib


class Cracker(QWidget, Ui_Cracker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hash Cracker")
        self.crack_button.clicked.connect(self.crack_pass)

    def crack_pass(self):

        flag = 0

        target_hash = self.hash.text()
        dropdown = self.comboBox.currentText()
        if dropdown == "wordlist":
            self.status_label.text("Cracking the Hash using the rockyou wordlist")

            with open('../Wordlist/rockyou.txt', 'rb') as infile:
                content = infile.read().decode('iso-8859-1')

                # Split the content into lines
                lines = content.splitlines()

                # Loop over each line
                for line in lines:
                    # Split the line into words
                    words = line.split()

                    # Loop over each word and check its MD5 hash
                    for word in words:
                        # Generate an MD5 hash of the word
                        hash_object = hashlib.md5(word.encode())
                        md5_hash = hash_object.hexdigest()

                        # If the hash matches the target hash, print the word
                        if md5_hash == target_hash:
                            self.textBrowser.setPlainText(word)
                    if flag == 1:
                        self.textBrowser.setPlainText("Password wasn't cracked")
        elif dropdown == "8 digit":
            flag = 0
            string = "Cracking password ............."
            self.status_label.setText("Cracking 8 digit password")

            target_hash = self.hash.text()
            with open('../Wordlist/0to9.txt', 'rb') as infile:
                content = infile.read().decode('iso-8859-1')

                # Split the content into lines
                lines = content.splitlines()

                # Loop over each line
                for line in lines:
                    # Split the line into words
                    words = line.split()

                    # Loop over each word and check its MD5 hash
                    for word in words:
                        # Generate an MD5 hash of the word
                        hash_object = hashlib.md5(word.encode())
                        md5_hash = hash_object.hexdigest()

                        # If the hash matches the target hash, print the word
                        if md5_hash == target_hash:
                            self.textBrowser.setPlainText(word)
                            flag = 1

                    if flag == 1:
                        self.textBrowser.setPlainText("Password wasn't cracked")
