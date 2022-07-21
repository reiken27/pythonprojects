import pyperclip
import re

text= pyperclip.paste()

def printemails():
    print('\nList of emails\n')
    for line in lst:
        print(line)

lst = re.findall("\S+@\S+",text)  #finds any e-mail adress in the text and stores it in a list
print('\n',len(lst),'e-mails have been found')

if len(lst) > 0:
    printemails()
    print('\n')

mylist= '\n'.join(lst)
pyperclip.copy(mylist)
print('Email have been copied to the clipboard\n')
# fasuionbfdi@gmail.com small text to find emails and test soadmi@hotmail.com  fdafafd qq 
