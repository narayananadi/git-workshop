arr = [1, 2, 3, 4, 5, 6, 8, 5, 3, 67, 3, 674, 87]
dictionary = {}
max_val = 0
max_num = ""
for x in arr:
    if str(x) not in dictionary:
        dictionary[str(x)] = 1
    else:
        dictionary[str(x)] += 1
    if dictionary[str(x)] > max_val:
        max_val = dictionary[str(x)]
        max_num = str(x)

print(max_num)
print(dictionary)
print(dictionary.keys())
