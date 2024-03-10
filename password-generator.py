# import string
# import random
# def passgen():
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.ascii_letters
#     s4 = string.digits
#     s5 = string.punctuation
#     print(s1)
#     print(s2)
#     print(s5)
#     print(s3)
#     print(s4)
#     print(s3)

















# practice
# import string
# import random

# def passgen():
#     s1 = string.ascii_letters
#     s2 = string.ascii_lowercase
#     s3 = string.ascii_uppercase
#     s4 = string.digits
#     s5 = string.hexdigits
  
    # print(s1)
    # print(s2)
    # print(s3)
    # print(s4)

    



# import string
# import random
# def passgen():
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.ascii_letters
#     s4 = string.digits
#     s5 = string.punctuation
#     pass_length = int(input("Enter the length of the password :\n"))
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#     s.extend(list(s5))
#     random.shuffle(s)
#     password = (" " .join(s[0:pass_length]))
#     print(password)
    
    
# passgen()

# practice 

import string
import random
def passgen():
    s1 = string.ascii_letters
    s2= string.ascii_lowercase
    s3= string.ascii_uppercase
    pass_length=int(input("Enter the length of your password: \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    password = (" ".join(s[0:pass_length]))
    print(password)
passgen()