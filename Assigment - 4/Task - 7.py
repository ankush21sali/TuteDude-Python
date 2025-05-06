try:
    with open("sample.txt", 'r') as file_read:
        for content in file_read:
            print(content)

except FileNotFoundError as e:
    print("The File",e.filename,"Was not Found.")

finally:
    print("Thank You!")
