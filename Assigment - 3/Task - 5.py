def factorial(num):
    sum = 1
    count = num

    while count > 1:
        sum *= count
        count -= 1

    return sum

num = int(input("Enter a Number : "))

result = factorial(num)
print("Factorial of",num,"is :",result)