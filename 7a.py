largest = None
smallest = None
num=0
while True:
    num = input("Enter a number or done: ")
    if num == "done":
        break
    try:
        number=int(num)
    except:
        print("Invalid input")
        continue
    if  smallest == None:
        smallest = number
    else:
        samllest = number
    if largest == None:
        largest = number
    elif number > largest:
        largest = number
    elif number < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)


