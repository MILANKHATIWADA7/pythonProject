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
print(t1[4])
print(t1[0][1])
print(t1[0][2])