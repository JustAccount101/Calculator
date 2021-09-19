#Calc ver. 1.0.0

operations = ["+", "-", "*", "/"]

what = ""
while not what in operations:
    what = input ("What operation? +, -, *, / ? ")
    if not what in operations:
        print ("Invalid operation!")


a = int ( input ("Enter the first number please: "))

b = int ( input ("Enter the second number please: "))

if what == "+":
    c = a + b
    print ("Result: " + str (c))
elif what == "-":
    c = a - b
    print ("Result: " + str (c))
elif what == "*":
    c = a * b
    print ("Result: " + str (c))
elif what == "/":
    c = a / b
    print ("Result: " + str (c))
