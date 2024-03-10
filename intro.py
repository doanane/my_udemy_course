# # x = 6
# # y = 7
# # print(x*y)
# # #this is a comment line
# # '''this is a pararaph comment'''
# # print(x**2)
# # m = "hello world"
# # print(m[6:9])
# # print(m.upper())
# # print(m.lower())
# # i = "Hello"
# # j = "World!"
# # print(i+ "",j)
# # k = "Dear"
# # print( i + " "+ k)
# # print(i+ "", j)
# # #1.1 tuple 1.2 list
# list
# # nums =[5,10,15,20,25,250]
# # nums.append(44)
# # nums.insert(2,33)
# # nums.sort()
# # nums.extend([32,23,34,55,56,73,56,43])
# # max(nums)
# # min(nums)
# # nums.append(99)
# # del nums[2:3]
# # list = ["desmond","opoku","anane","blessing","samuel",33,"boakye"]
# # list2 = ['bismark','ephraim','micheal']
# # list.remove("desmond")
# # nums.remove(25)
# # keys = ['bismark','ephraim','micheal']
# # values = [1, 2, 3]
# # combo = dict(zip(keys, values))
# # list2 = list2 + list
# # print(list2)
# # print(nums)
# # print(combo)
# # tuple3 =("apple","kiwi","banana","pear","orange")
# # y = list(tuple3)
# # y[3] = "water melon"
# # tuple3 = tuple(y)
# # print(tuple3)

# # tuple1 = ("mom","dad","siblings","son","daugther","wife")
# # x = list(tuple1)
# # x.insert(4,"grandma")
# # tuple1 = tuple(x)
# # print(tuple1)


# keys = ["one","two","three","four","five","six", "car"]
# values = [1,2,3,4,5,6,"nissan"]
# combo = dict(zip(keys, values))
# x = combo.items()
# y = combo.values()
# combo.update({"car":"toyota"})
# # format for updating values with the help of update method.

# #how to add a function to a dictionary
# combo["color"] = "blue"

# # how to remove a function from a dictionary
# combo.pop("car")

# print(combo)
# print(x)

# # tuple6 = ("one","two","three","four",77)
# # x = list(tuple6)
# # tuple6 = tuple(x)
# # print(tuple6)

#convertion of numeric data types
# a = 10.77
# b = int(a)
# print(b)
# c = 998.97
# d = complex(c)
# print(d)
# e =789
# f = float(e)
# print(f)
# showing time 
# import datetime
# time = datetime.datetime.now()
# print(time)
#showing user time every second using while loop
# import datetime
# from time import sleep
# while True:
#   time = datetime.datetime.now()

#   print(time)
#   sleep(5)

# Conditional statement
# if else
# num = 9
# if num == 0:
#   print("this is an even number")
# elif num%2 == 0:
#     print("this is a divisible number")

# else:
#     print("this is a odd number")

# loops in python
# while loop and for loop
# while loop is used to repeat multiple same code mant times until you tell the code to stop a some point.
# i = 1 
# while i <10:
#   print(i)
#   i +=1

# i = 1 
# while i <10:
#   print("sey")
#   i +=1

#to combine two more words using while loop.
# i = 1
# j = 1
# while i <5:
#   print("desmond", end=" ")
#   while j<5:
#     print("opoku", end=" ")
#     j +=1
#   i +=1


# for loop
# num = 5
# for x in range(12):
#   print(num*x)
  
# x = ["desmond",1,2,3,4,8]
# for i in x:
#     print(i)
#for i in range(11):
# def add(num1, num2):
#   sum = num1 + num2
#   return sum
# num1 =int(input("Enter value 1 to add"))
# num2 =int(input("Enter value 2 to add"))
# print(add(num1, num2))

# def greet(name):
#   print("hello an how're you doing?",name);
# greet('Dannnysara')

#try accept block
#x = 5
# try:
#   print(x)
# except Exception as e:
#   print(e)

# How to do file handling in pthon
# f = open("intro2.py","r")
# print(f.read(20))
# f.close()