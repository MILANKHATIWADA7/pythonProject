# # # import test as t
# # #
# # # t.add()
# #
# # from test import add # direct folder ko function call garxa
# # add()
# #
# #
#
#
# def summation(a, b):
#     c = a + b + 3
#    # print(f"sum is {c}")
#     return c
#
#
# res = summation(22, 33) #return garda res ma ca ko value return hunxa
# print(f"sum is {res}")
#
# assert summation(2, 3) == 5, 'There seems to be some issues 2 and 3 should be 5'
# print("Everything appears to be good")
#


# def list_test(some_list):
#     # print(some_list)
#     return some_list
#
#
# check_info = list_test([2, 5, 9, 8, 7, 99])
# print(check_info)
#
#
# assert list_test([4, 5, 5]) == [4, 5, 5], 'Issues are there' #QA ko lagi important hunxa
# print("Everything is alright")

#
# def list_test(some_list):
#     # print(some_list)
#     # print(max(some_list))
#     max_number = some_list[0]
#     for i in some_list:
#         if max_number < i:
#             max_number = i
#     print("Largest number is", max_number)
#
#
# list_test([1, 2, 3, 7, 99, 5])


# def list_check(some_list):
#     print(some_list)
#     print(max(some_list))
#     return some_list
#
#
# assert list_check([1, 2 ,3]) == [1, 2, 3], 'Issues are their'
# print("Everything is all good")


#Return lay kasari kam garxa ta

# def add(num1, num2):
#     result = num1 + num2
#     return result
#
#
# print(add(22, 33))


#Assert is used to verify the correctness by the developer

# def check_list(some_list):
#     # print(some_list)
#     return some_list
#
#
# assert check_list([100,2,3,4]) == [100,2,3,4], 'Problem is their'
# print("Every thing is all good")
# print(check_list([1,2,3,4,5,6]))


#Another day

#Roundoff ko lagi
# s1 = 'Math'
# s2 = 'Science'
# s3 = 'English'
# m1 = float(input(f"Enter mark1 of {s1} "))
# m2 = float(input(f"Enter mark of {s2} "))
# m3 = float(input(f"Enter mark of {s3} "))
# total = m1 + m2 + m3
# print(f"Total is {total}")
# per = total/3
# #per = round(per, 2)
# #per = per.__round__(2)
# print("%.4f" %per)
# print(f'Scored percent is {per}%')


#from math import ceil, floor # one of the way to import
# import math as m
#
# print(2 + 3)
# print(2 * 3)
# print(2 ** 3)
# print(pow(2,3))
# print(m.ceil(3.1))
# print(m.floor(3.3))
#
#
# print(f'Factorial of 5 is{m.factorial(5)}')


# l1 = [["ram", 22, 77.5], ["shyam", 23, 88.5], ["hari", 19, 91]]
# l1.append(["sita", 18, 80])
# print(l1)
# print(len(l1))


#TUPLE used for immutable data
#Tuple vitra ni list banauna milxa jo chai mutable hunxa tara tuple cahi immutable hunxa
t1 = (['apple', 'banana', 'orange'],'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 33)
print(type(t1))
print(t1)
print(len(t1))
print(t1[0:3])
print(t1[0])
t1[0][0] = 'mango'
print(t1)
print(t1[0][1])
print(t1[0][2])

