def factorial(num):
    fact = 1
    count = num

    while count > 1:
        fact *= count
        count -= 1

    return fact

num = int(input("Enter a Number : "))

result = factorial(num)
print("Factorial of",num,"is :",result)
