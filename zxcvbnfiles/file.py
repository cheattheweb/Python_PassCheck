from zxcvbn import zxcvbn
from zxcvbn.matching import add_frequency_lists

add_frequency_lists({
    'my_list': ['arka', 'barua'],
    'another_list': ['baz']
})
li = ['kajal','barua']
password = input("Password : ")
name = input("Name : ")
name = name.split()

result = zxcvbn(password, user_inputs=li+name)
print(result)
