# f = open("test.txt",'r')
# f.close()
# print("This is remaining work!")


# Try, except, else, finally (teef)
# try:
#     a = 22 / 0
#     print(a)
# except Exception as ex:
#     print(f"Their is error {ex}")
# else:   #yo chai error na aai chalda yo else ma janxa
#     print("We are on next stuff")
# finally: #Each an every time ma janxa yo block ma chai
#     print("This is try except block")
# print("This is demo")


# try:
#     f = open("test1.txt", 'r')  # read(r), write(r), append(a), create(x)
#     #data = f.readline() #single line read garxa test1.txt bata
#     data = f.readlines() #sab read garxa
#     # data = f.read()
#     print(data)
#     print(type(data))
#     print(data[0:3])
#     f.close()
# except Exception as ex:
#     print(f"Error on file {ex}")
# else:
#     print("Inside file")
# print("This is remaining work!")


age = int(input("Enter your age: "))
print(f"{age}")

