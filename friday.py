# DAY-6 ( check odd and even )

# a = int(input("Enter any number:"))
# if a != 0:
#     if a % 2 == 0:
#         print("Entered number is even number")
#     else:
#         print("Entered number is odd number")
# else:
#     print("Entered number is zero")


# LOOP

# infinite loop
# a = 22 > 5
# while a:
#     print("hello", end='')
#

# finite loop
# a = 1
# while a <= 3:
#     print("Hello world")
#     a = a + 1
# print("Outside the loop is ", a)


# a = 50
# while a <= 60:
#     print(a, end=' ')
#     a = a + 1

# a = int(input("Enter the start value:"))
# num = int(input("Enter the end value:"))
# upd = int(input("Enter the updated value:"))
# while a <= num:
#     print(a,end=' ')
#     a = a + upd

#
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# if num1 > num2:
#     print("num1 is grater")
# elif num1 == num2:
#     print("Both numbers are equal")
# else:
#     print("num2 is grater")


# nationality = input("Enter the nationality: ")
# if nationality == "nepali":
#     print("matched")
# elif nationality == "bideshi":
#     print("Thekai xa")
# else:
#     print("Mars is there")


# i = 1
# while i <= 3:
#     print("This is count number", i)
#     nationality = input("Enter the nationality: ")
#     if nationality == "nepali":
#         print("matched")
#     elif nationality == "bideshi":
#         print("Thekai xa")
#     else:
#         print("Mars is there")
#     i += 1


# product1 = int(input("Enter the cost of product1:"))
# product2 = int(input("Enter the cost of product2:"))
# product3 = int(input("Enter the cost of product3:"))
# total = product1 + product2 + product3
# print("Total cost of all products is", total)
# pay_amount = int(input("Make a payment: "))
# differance = pay_amount - total
# # print("The differance is:", -differance)
# if differance >= 0:
#     if differance > 0:
#         print("Thanks!! Your change is", differance)
#     else:
#         print("Thanks!! Visit us again!!")
# else:
#     differance = -differance
#     print("Insufficient amount!!")
#     pay_amount_left= differance - pay_amount
#     print("Remaining payment is", differance)
#     pay_amount = int(input("Make a payment again:"))
#     pay_amount_left = pay_amount - differance
#     if pay_amount_left >=0:
#         if pay_amount_left >0:
#             print("Thanks!! Your change is", pay_amount_left)
#         else:
#             print("Thanks!!")
#     else:
#         print("Pagal ho tapai!!")


# shirt = int(input("Enter the cost of shirt: "))
# pant = int(input("Enter the cost of pant: "))
# total_cost = shirt + pant
# print("your total cost is ", total_cost)
# paid_amount = int(input("Enter the amount to be paid: "))
# while paid_amount < total_cost:
#     difference = total_cost - paid_amount
#     print("Insufficient amount, please pay" + str(difference) + "more")
#     repaid = int(input("Enter additional amount: "))
#     paid_amount = paid_amount + repaid
# if paid_amount > total_cost:
#     print("return change = ", paid_amount - total_cost)
#     print("Thank you for shopping with us")
# else:
#     print("Thank you for shopping with us")

# DAY-7


#While loop

# i = 1
# while i<= 5:
#     print("\t\t Student number", 1)
#     mark1 = float(input("Enter the mark1"))
#     mark2 = float(input("Enter the mark2"))
#     total = mark1 + mark2
#     per = total/2
#     print("Scored percent is", per)
#     if per >= 32:
#         print("Pass")
#     else:
#         print("Try again")
#     i = i + 1

#multiplication table
# i = 1
# num = int(input("Which number multiplication table do you want:"))
# while i <= 10:
#     value =  num * i
#     print(num, "*", i, "=", value)
#     i = i + 1

# i = 1
# j = 1
# while j <= 3:
#     num = int(input("Which number multiplication table do you want:"))
#     while i <= 10:
#         value =  num * i
#         print(num, "*", i, "=", value)
#         i = i + 1
#     j = j + 1
#


# i = 1
# while i <= 3:
#     j = 1
#     print("i is here", i)
#     while j <= 2:
#         k = 1
#         print("\t\t j is here", j)
#         while k <= 2:
#             print("\t\t k is here", k)
#             k = k + 1
#         j = j + 1
#     i = i + 1
#
#
# #WAP multiplication from 1 to 10
#
#

# i= 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(str(i) + "*" + str(j) + "=", i*j ) # type caste garya integer kai string banako (string ra sint concatinate hudaina so)
#         j = j+1
#     print("\t\t\t")
#     i = i + 1


#DAY-8

#For LOOP

# for i in range (1,12):
#     print("QUestion number", i)


# for i in range (1, 12, 3): #3 jump hunxa 1 4 7 10
#     print("Question number", i)
#     print(type(i))

# for i in range (1, 12, 3): #3 jump hunxa 1 4 7 10
#     print("Question number", i)
#     print(type(i))


# result = 1
# name = input("Enter a name:")
# num = int(input("Whose factorial is needed:"))
# for i in range (1, num+1):
#     print(i)
#     result = result * 1
# print(f"Factorial of {num} asked by {name} is {result}") #string formatting bata garya


# i = 1
# sum_odd = 0
# sum_even = 0
# while i  <= 10:
#     if i % 2 == 0:
#         sum_even = sum_even + i
#     else:
#         sum_odd += i
#     i += 1
# print(f"Sum of even number is {sum_even}")
# print(f"Sum of odd number is {sum_odd}")
# if sum_even > sum_odd:
#     print("Sum even is grater")
# else:
#     print("sum odd is grater")