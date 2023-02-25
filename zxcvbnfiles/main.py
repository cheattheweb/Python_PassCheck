from typing import List

from zxcvbn.matching import add_frequency_lists
from zxcvbn import zxcvbn
import re

with open('/home/arka/Github/Python_PassCheck/Wordlist/MESCollege.txt') as f:
    lines = f.read().splitlines()
    passwords = []
    for line in lines:
        # split line based on spaces and commas using regular expression
        split_line = re.split(r'[ ,]+', line)
        passwords += split_line


print(len(passwords))
password = input("Password : ")
name = input("User Name : ")

name = name.split()

result = zxcvbn(password, user_inputs=name+passwords)

print(result)
