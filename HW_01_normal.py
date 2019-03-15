#task 1
x=int(input("Enter number:"))
while x < 0 or x > 10:
    print("Incorrect. Number must be in range 0 - 10")
    x=int(input("Enter number:"))
x = x**2
print (x)

#task 2
a=raw_input("Enter 1st parameter:")
b=raw_input("Enter 2nd parameter:")
new_a=b
new_b=a
print("1st parameter: "+new_a)
print("2nd parameter: "+new_b)