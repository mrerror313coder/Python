# # import math
# # def isPrime(n):
# #
# #     for j in range(2, n):
# #         if (n%j == 0):
# #             return False
# #     return True
# # def getRange(start, end):
# #     count =0
# #     total = 0
# #     for i in range(start,end) :
# #         a=isPrime(i)
# #         if(a==True) :
# #             print(i,end=" ")
# #             count+=1
# #             total+=(math.log(i))
# #     print("Total Prime Numbers From",start,"To",end,"Are",count)
# #     return total
# #
# # a=getRange(2,50)
# # b=getRange(51,100)
# # c=getRange(101,150)
# # d=getRange(151,200)
# # e=getRange(201,250)
# # f=getRange(251,300)
# # g=getRange(301,350)
# # h=getRange(351,400)
# # i=getRange(401,450)
# # sumOfPrimeLogs=a+b+c+d+e+f+g+h+i
# # print("Sum of Logs is ",sumOfPrimeLogs)
# # print("Ratio is ",(sumOfPrimeLogs)/450)
#
#
#
# # f = int(input("Enter a number: "))
# # x=0
# # y=1
# # z=0
# # for i in range(0,f+1):
# #     print(z,end=" ")
# #     x=y
# #     y=z
# #     z=x+y
#
# # f = int(input("Enter a number: "))
# # l = [0,1]
# # for i in range(2,f+1):
# #     l.append(l[i-1]+l[i-2])
# #
# # print(l,end=" ")
#
# # i = int(input("Enter Size of List: "))
# # l=[]
# # for j in range(1,i+1):
# #     l.append(int(input("Enter Element ")))
# # print("You Entered List Elements : ",l,end=" ")
# # print()
# # l.sort()
# # print("Sorted List is : ",l)
# # print("Maximum Value in List is :",max(l))
# # print("Minimum Value in List is :",min(l))
# # print("sum of Value in List is :",sum(l))
# # print("Average Value in List is :",sum(l)/len(l))
#
#
# # d = {
# #     'Name':'Asad',
# #     'Roll No':313
# # }
# # print(d)
# # d['Class']='BS CS'
# # print(d)
# # print(d['Name'])
#
#
# # s=input("Enter a string: ")
# # print(s)
# # print(s.upper())
# # print(s.lower())
# # print(s.replace(" ", "-"))
# # print(s)
#
# # def cale(a,b,opr):
# #     if opr == '+':
# #         return a+b
# #     elif opr == '-':
# #         return a-b
# #     elif opr == '*':
# #         return a*b
# #     elif opr == '/':
# #         return a/b
# #     else :
# #         return "Invalid Operation"
# #
# # first=int(input("Enter First Number: "))
# # second=int(input("Enter Second Number: "))
# # operation=input("Enter Operation: ")
# # ans=cale(first,second,operation)
# # print(ans)
#
# """f=open("Enjoy.txt",'w')
# if f:
#     print("File Successfully Opened")
# print(type(f))
# f.close()"""
#
# '''f=open("D:/txtfiles/E.txt",'w') """ \ not used in Python Windows"""
# if f:
#     print("File Successfully Opened")
# print(type(f))
# f.close()'''
#
# '''f=open("D:/txtfiles/Enjoy.txt",mode='r',buffering=10,encoding='utf-8')
# if f:
#     print("Opened")
# print(f)
# f.close()'''
#
# '''f=open("D:/txtfiles/Enjoy.txt",mode='r',buffering=10)
# if f:
#     print("Opened")
# print(f)
# f.close()'''
# ''' After close mode change from 'r' to 'w' '''
# '''f=open("D:/txtfiles/Enjoy.txt",mode='w',buffering=10)
#
# print("File name is : ",f.name)
# print(f.mode)
# print(f.encoding)
# print("Is file closed?",f.closed)
# f.close()
# print("Is file closed?",f.closed)
# print(f.mode)'''
#
# '''f=open("D:/txtfiles/Enjoy.txt",mode='r',buffering=10)
# print(f.readable())
# print(f.writable())
# f.close()'''
#
# '''f=open("D:/txtfiles/Enjoy.txt",mode='w+',buffering=10)
# print(f.readable())
# print(f.writable())
# f.close()'''
#
# '''f=open("D:/txtfiles/Enjoy.txt",mode='r',buffering=10)
# if f.readable():
#     print("File is Readable")
#
# f.close()'''
#
# '''f=open("Enjoy.txt")
# f.close()'''
# '''
# import os
# if os.path.isfile("Enjoy.txt"):
#     f=open("Enjoy.txt")
#     print("File Exist")
# else :
#     print("File not Exist")
# f.close()
# '''
#
# """import os
# filename=input("Enter File Name : ")
# if os.path.isfile(filename):
#     f=open(filename)
#     print("File Exist")
# else :
#     print("File not Exist")
# f.close()
# """
# '''
# import os
# try:
#     filename=input("Enter File Name : ")
#     if os.path.isfile(filename):
#         f=open(filename)
#         print("File Exist")
#     else :
#         print("File not Exist")
#         f=None
# finally:
#     if f:
#         f.close()
# '''
# """
# import os
# with open("D:/txtfiles/Enjoy.txt",mode='r',buffering=10) as f:
#     if f.readable():
#         print("File is Readable")
# """
# import math
# def isPrime(n):
#
#     for j in range(2, n):
#         if (n%j == 0):
#             return False
#     return True
# def getRange(start, end):
#     count =0
#     total = 0
#     while start<end :
#         i=start
#         a=isPrime(i)
#         if(a==True) :
#             print(i,end=" ")
#             count+=1
#             total+=(math.log(i))
#         start+=1
#     print("Total Prime Numbers From",start,"To",end,"Are",count)
#     return total
#
# a=getRange(2,50)
# b=getRange(51,100)
# c=getRange(101,150)
# d=getRange(151,200)
# e=getRange(201,250)
# f=getRange(251,300)
# g=getRange(301,350)
# h=getRange(351,400)
# i=getRange(401,450)
# sumOfPrimeLogs=a+b+c+d+e+f+g+h+i
# print("Sum of Logs is ",sumOfPrimeLogs)
# print("Ratio is ",(sumOfPrimeLogs)/450)
#






#print("Hello World " * 5)

# x = ['Asad', 'Ali', 'Khan']
# x.insert(0, 'Muhammad') # For insert element in List
# x.remove('Ali')    # For remove element from List
# z = x.index('Khan')  # Gives the index number of List element
# print(x)
# print(z)



# from math import *
# print(sqrt(25))
# print(sqrt(2))
# print(ceil(78.73))  # The ceil() method in Python is used to return the smallest integer greater than or equal to a given number. It is part of the math module, so you need to import the module before using the method.
# print(floor(78.73)) # The floor() method in Python is used to return the largest integer less than or equal to a given number. Like ceil(), it is part of the math module, so you need to import the module before using the method
# print(round(78.73)) # The round() function in Python is used to round a floating-point number to a specified number of digits. If no number of digits is provided, it rounds the number to the nearest integer.
# print(pow(5, 5)) # The pow() function in Python is used to calculate the power of a number. It raises a number to the power of another number and optionally performs modulo operation.
# print(max(7,24,3)) # The max() function in Python is used to find the largest item in an iterable or the largest of two or more arguments.
# print(min(7,24,3)) # The min() function in Python is used to find the smallest item in an iterable or the smallest of two or more arguments.


# x= [12, 3, 33, -3, 15,2]
# x.sort()  # The sort() method in Python is used to sort the elements of a list in place. This means that it modifies the original list and does not return a new list.
# print(x)
# temp=x
# y=list(temp)
# y.remove(15)
# print(y, temp)

# def sum_all(*x) :
#     sum = 0
#     for i in x:
#         sum += i
#     return sum
# print("Sum is",sum_all(33, 77, 44, 35, 76))

# x =[
#     [1, 2, 4, 7],
#     [3, 1, 3],
#     [3, 1, 6]
# ]
# print(x[1]) # [3, 1, 3]
# print(x[0][3]) # 7
# print(max(x))

# import math
# print(dir(math))
# help(math)
# print(math,__doc__)

# f=open(r"C:\Users\M Hamza Mirani\PycharmProjects\MR.ERROR313\first.txt","r")
# print(f.read())
# f.close()
#
# fh=open(r"C:\Users\M Hamza Mirani\PycharmProjects\MR.ERROR313\first.txt","w")
# fh.write("Asad")
# print(fh)
# fh.close()
#
# fr = open(r"C:\Users\M Hamza Mirani\PycharmProjects\MR.ERROR313\first.txt","r")
# print(fr.read())
# fr.close()

# fr = open(r"a.txt","w")
# fr.writelines("Hussain (R.A) ibn Ali (R.A) de katil zaleel rahsin khawaar rahsin\n Aa saal poora maheeny saary na thiek theesen bimaar sahsin\n Ali (R.A) de bachry de kally katil bikaar loog hin bikaar rahsin")
# fr.close()
#
# fr = open(r"a.txt","r")
# read =fr.readlines(3)
# print(read)
# fr.close()

# x = ['Asad', 'Ali', 'Khan']
# for i in x:  # Looping each element in the List
#     print(i) # Asad Ali Khan
#     for j in i: # Looping each the element in String
#         print(j) # Asad Ali Khan


# while True:
#     try:
#         x = int(input('Enter a number: '))
#         total = x * 5
#         print(total)
#         break
#     #except ValueError:
#     except Exception:
#         print('Please Enter a number')
#     finally:
#         print("ENJOY CODING")


# def anywordcount(filename,findword) :
#     try:
#         f=open(filename,'r')
#         read=f.readlines() # ['Hussain (R.A) ibn Ali (R.A) de katil zaleel rahsin khawaar rahsin\n', ' Aa saal poora maheeny saary na thiek theesen bimaar sahsin\n', ' Ali (R.A) de bachry de kally katil bikaar loog hin bikaar rahsin']
#         f.close()
#         for word in findword:
#             word=word.lower() # ali
#             count=0
#             for sentence in read:  # Hussain (R.A) ibn Ali (R.A) de katil zaleel rahsin khawaar rahsin
#                 line=sentence.split() # ['Hussain', '(R.A)', 'ibn', 'Ali', '(R.A)', 'de', 'katil', 'zaleel', 'rahsin', 'khawaar', 'rahsin']
#                 for each in line: # Hussain
#                     line2=each.lower() # hussain
#                     line2=line2.strip(";,.!@#$%^&*\n")
#                     if line2 == word:
#                         count+=1
#             print(word," : ",count)
#     except FileNotFoundError:
#         print("File Not Found")
# anywordcount("a.txt",["Ali"])

# def anywordcount(filename,findword) :
#     try:
#         f=open(filename,'r')
#         read=f.readlines()
#         f.close()
#         for word in findword:
#             word=word.lower()
#             count=0
#             for sentence in read:
#                 line=sentence.split()
#                 for each in line:
#                     line2=each.lower()
#                     line2=line2.strip(";,.!@#$%^&*\n")
#                     if line2 == word:
#                         count+=1
#             print(word," : ",count)
#     except FileNotFoundError:
#         print("File Not Found")
# anywordcount("a.txt",["Ali"])

# a = {2, 5, 6, 2, 12}
# print(a)
# a.add(666)
# print(a)
# a.add(33)
# print(a)
# a.discard(66)
# print(a)
# a.remove(5)
# print(a)
# #a.remove(65)  # not Allowed

# # Sets
# x = {1, 4, 3, 7, 5}
# y = {4, 1, 5, 2, 9}
# m = x.union(y)
# print(m)
# m = y.union(x)
# print(m)
# m = x.intersection(y)
# print(m)
# m = y.intersection(x)
# print(m)
# m = x.difference(y)
# print(m)
# m = y.difference(x)
# print(m)


# # Dictionary
# x = {"mo":19, "Ali":15 }
# for k,v in x.items():
#     print(k, v)
# for k in x.keys():
#     print(k)
# for v in x.values():
#     print(v)
# for k,v in x.items():
#     print(k)
#     print(v)
# print(x['Ali'])


# x ={}
# x["Saad"]=313
# x["Asad"]=12
# print(x)
# x.pop("Saad")
# print(x)
# x["Arham"]=92
# print(x)
# del x["Arham"]
# print(x)
# x["Akhlaq"]=666
# print(x)
# x.clear()
# print(x)








