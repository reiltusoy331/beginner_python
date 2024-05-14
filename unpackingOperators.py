values1 = list(range(5))
values2 = [*range(5), *"hello"]

first = [1,2]
second = [3,4]
print(*first,*second)