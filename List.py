# # #list
# #
# # name = ['ram', 'shyam', 'hari', 'sita']
# # print(name)
# #
# # name.append("gita")
# # print(name)
# #
# # name.append("rita")
# # print(name)
# #
# # name.insert(1, "nisha")
# # print(name)
# #
# # print(type(name[0]))
# # print(len(name))
#
#
# # name = ['ram', 'shyam', 'hari', 'sita']
# # print(name)
# #
# # name.append("gita")
# # print(name)
# #
# # name.append("rita")
# # print(name)
# #
# # name.insert(1, "nisha")
# # print(name)
# #
# # print(type(name[0]))
# # print(len(name))
# #
# # print(name[0:5])#slicing
# #
# # print(name[0:7:2])
# #
# # #support duplication
# #
# # #name check
# # user_check_name = input("Enter the name to check:")
# # if user_check_name in name:
# #     print("This person is present")
# # else:
# #     print("This person is not here")
#
#
# # my_list = ['ram', True, 22, 22.5, 'ktm']
# # print(type(my_list))
# # print(my_list)
#
#
# # #Sorting
# # my_list = [77, 88 ,51, 18, 41, 81]
# # my_list.sort()
# # print(my_list)
#
#
# # my_list = ['avengers', 'spiderman', 'starwars', 'batmsn', 'thor', 'avangers', 'kabaddi']
# # print(my_list)
# # #my_list[0] = 'kanchana'
# # my_list.append('kanchana')
# # my_list.append('EvilDead')
# # my_list.insert(1, 'titanic')
# # print(my_list)
#
# my_list0 = []
# my_list1 = ['avengers', 'infinityear', 'Thor']
# my_list2 = ['Batman', 'titanisc', 'EvilDead']
# my_list0 = my_list2.copy()
# print(my_list1+1)

# # # function ma suru Statement wa block of statement ma kam garxa
#
# a = 22
# b = 33
# def addition():
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
#     c = a + b
#     print(f"Sum is", c)
#
#
# def sub():
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
#     c = a - b
#     print("Diff is", c)
#
#
# addition()
# sub()
#
#
# list1 = ['ram', 'shyam', 'hari']
# print(list1)
# list1.append('sita')
# list1.insert(2, 'nisha')
# print(list1)
# list1.sort()
# print(list1)
#
# list1.sort(reverse=True)
# print(list1)

#NESTED LIST

# l1= [['ram', 22, 75],
#      ['shyam', 23, 76],
#      ['hari', 24, 77]]
# print(l1)
# l1.append(['sita', 19, 78])
# print(l1)


# l1 = []
# n = int(input("Kati jana ko detail rakhnay? "))
# for i in range(n):
#     new_list = []
#     name = input("Enter a name: ")
#     age = int(input("Enter your age: "))
#     mark = float(input("Enter your mark: "))
#     new_list.append(name)
#     new_list.append(age)
#     new_list.append(mark)
#     l1.append(new_list)
# print(l1)


comp_location = r"c:\\users\\admin\\milan" #To print the raw value
print(comp_location)


