# 1 Multiplication from 1 to 10

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(str(i) + "*" + str(j) + "=", i*j)
#         j = j + 1
#     print("\t\t\t")
#     i = i + 1
#


# 2 ask user range of table

# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
#
# print(f"Multiplication table from {start} to {end} is as follow:")
#
# i = start
# while i <= end:
#     print(f"\nMultiplication table of {i}:")
#     j = 1
#     while j <= 10:
#         print(f"{i} * {j} = {i * j}")
#         j += 1
#     i += 1


#3 check wheather entered number is odd or even

# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Entered number is even")
# else:
#     print("Entered number is odd")


#4 Largest numbera among two number

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
#
# if number1 > number2:
#     largest_number = number1
# else:
#     largest_number = number2
#
# print("The largest number is:", largest_number)

#5 Largest numbera among entered three number
#
# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# number3 = float(input("Enter the third number: "))
#
# if number1 >= number2 and number1 >= number3:
#     largest_number = number1
# elif number2 >=  number1 and number2 >= number3:
#     largest_number = number2
# else:
#     largest_number = number3
# print("The largest number is:", largest_number)
#
#


#6 Display 1 to 50 using loop

# a = 1
# while a <= 50:
#     print(a, end=' ')
#     a = a + 1


#7 Display even number that lies between 1 to 50

# a = 1
# while a <= 50:
#     if a % 2 == 0:
#         print(a, end=' ')
#     a = a + 1


#8 Display odd numbers that lies between 1 to 50

# a = 1
# while a <= 50:
#     if a % 2 ==1:
#         print(a, end=' ')
#     a = a + 1

#9 Calculate the sum of even numbers and odd numbers that lies in range 1 to 10 and show which is grater

i = 1
sum_odd = 0
sum_even = 0
while i  <= 4:
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd += i
    i += 1
print(f"Sum of even number is {sum_even}")
print(f"Sum of odd number is {sum_odd}")
if sum_even > sum_odd:
    print("Sum even is grater")
else:
    print("sum odd is grater")

    (f"")