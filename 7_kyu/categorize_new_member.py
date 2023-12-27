category_1 = "Senior" # 55+, 7+
category_2 = "Open" # 55-, 7-
output = []

age_range_1 = list(range(55, 200)) # 55+
age_range_2 = list(range(1, 55)) # 55-

hahdicap_range_1 = list(range(8, 27)) # 7+
hahdicap_range_2 = list(range(-2, 7
                              )) # 7-

list_members = [[78, -2], [80, 20], [1, -2], [55, 26]]

in_1 = 0
in_2 = 0
in_3 = 1

for value in list_members:
    if list_members[in_1][in_2] in age_range_1 and list_members[in_1][in_3] in hahdicap_range_1:
        output.append(category_1)
    else:
        output.append(category_2)
    in_1 += 1

print(output)