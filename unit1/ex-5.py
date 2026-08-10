numbers = [10,20,30,40,50]

print(numbers)
print("First Element :",numbers[0])
print("Slice :",numbers[1:4])

numbers.append(60)
print("After append :",numbers)

square = [x*x for x in numbers]
print("Square :",square)
