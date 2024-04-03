items =[("Product1",10),
        ("Product2",20),
        ("Product3",30),
]


x = list(filter(lambda item: item[1] >= 20, items))
print(x)