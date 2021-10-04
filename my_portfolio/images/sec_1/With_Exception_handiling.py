x=int(input("enter first number "))
y=int(input("enter second number "))

try:
    z=x/y
except Exception as e:
    print (e,"exception occured")

print("result is", z)
print("progrem excecuted perfectly")