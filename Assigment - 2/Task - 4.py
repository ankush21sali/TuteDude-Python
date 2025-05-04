start_val = int(input("Enter the Start Val of Sum : "))
end_val = int(input("Enter the End val of sum : "))

sum = 0

for i in range(start_val, end_val + 1):
    sum += i

print('The sum of number from',start_val,'to',end_val,'is :', sum)