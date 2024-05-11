numbers =[1,1,2,3,4]
first = set(numbers)
second = {1,5}

print("Values of first Sets: ",first)
print("Values of second Sets: ",second,"\n")

print("UNION of first & second sets.")
print(first | second,"\n")

print("INTERSECTION of first & second sets.")
print(first & second,"\n")

print("DIFFERENCE of first & second sets.")
print(first - second,"\n")

print("SYMMETRIC DIFFERENCE of first & second sets.")
print(first ^ second,"\n")