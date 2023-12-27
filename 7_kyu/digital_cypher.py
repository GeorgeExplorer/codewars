message = ["a", "b", "c", "d", "e", "f"]
output = []
key = 240
i = 0
pie_key = [int(item) for item in str(key)]
print(pie_key)

for character in message:
    number = ord(character) + pie_key[i] - 96
    output.append(number)
    i = (i + 1) % len(pie_key)
print(output)
