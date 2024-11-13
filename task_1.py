numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_of_none = 4
sum_without_none = sum(numbers[:4] + numbers[5:])
count = len(numbers)
average = sum_without_none / count
numbers[index_of_none] = average
print("Измененный список:",numbers)
