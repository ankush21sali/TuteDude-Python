with open("output.txt","w") as output_file:
    data = input("Enter test to write to the file : ")
    output_file.write(data)
    print("Data successfully Written to Output.txt")

with open("output.txt",'a') as output_file:
    data = input("Enter additional text to append : ")
    output_file.write("\n" + data)
    print("Data successfully appended.")

with open("output.txt", "r") as output_file:
    print("Final Content of output.txt : ")
    for lines in output_file:
        print(lines)