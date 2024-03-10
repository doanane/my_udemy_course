
import string
import random
from csv import writer
# head = ['platform','password']
# with open('pass.csv','w') as f:
#     writedata = writer(f)
#     writedata.writerow(head)
def passgen():
    s1 = string.ascii_letters
    s2= string.ascii_lowercase
    s3= string.ascii_uppercase
    platform =input("Enter name of platform: \n")
    pass_length=int(input("Enter the length of your password: \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
    password = (" ".join(s[0:pass_length]))
    print(password)
    passdata = [platform,password]
    with open('pass.csv','a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)
passgen()