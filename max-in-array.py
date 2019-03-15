numbers = []
max = None
for value in range(1, 6) :
    number = int(input("Please enter number : "))
    if ((max is None) or ( number > max)):
        max = number
    numbers.append(number)
print ("Max values : ",max)
