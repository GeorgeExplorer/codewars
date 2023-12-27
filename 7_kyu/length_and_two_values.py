n = 5
value_1 = "four"
value_2 = True

list = []

while len(list) < n:
        list.append(value_1)
        if len(list) < n:
            list.append(value_2)
        while len(list) == n:
            break
print(list)