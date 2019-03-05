def add_2(list):
    list[0] = 999
    list.append(10)
    list.append(20)


x = [10, 20, 30]
add_2(x)
print(x)
