
# Introduction

print("Hello, it is AREA CALCULATOR")
print()
print("My name is Ahon")
print()
print("You can calculate any area releated problem.")
print()
input("Press enter to continue...")

# Asking conditions

import math

print("Write the releated thing in capital form from given bellow :")

print()

print("1. CIRCLE ")
print("2. CONE")
print("3. Cylinder")
print("4. ROOT OF A NUMBER")

t = input("Enter the thing :-")

# Calculation

if ( t == "CIRCLE") : 
    T = input("Do you have question releated to Area ? ( YES/NO ) :")
    if ( T == "NO") :
        print()
        print("OK !")
        print()
    
    elif ( T == "YES") :
        print()
        
        r = input("Enter the Radius :")
        print()
        print("Ok, Radius is ", r)
        
        PNUM = float( r ) 
        
        Circumference = 2 * math.pi * PNUM
        print("Circumference is ", Circumference)
        A = PNUM ** 2
        Area = math.pi * A
        print("Area is ", Area)
        r = PNUM ** 3
        V = 4/3 * math.pi * r
        print("Volume is ", V )
    else :
        print("Enter only valid value")
elif ( t == "CONE") :
    r = input("Enter the Radius")
    print()
    print("Ok, your radius is ", r)
    h1 = float(input("Enter the curved hieght"))
    RNUM = float(r) ** 2
    h = math.sqr(RNUM + h1 ** 2)
    ground_area = math.pi * RNUM
    Outside_Area = math.pi * r * h1
    Volume = 1/3 * math.pi * RNUM * h
    print("Ground area is ", ground_area)
    print("Outside Area is ", Outside_Area)
    print("Volume is ", Volume)
elif ( t == "Cylinder") :
    r = input("Enter the Radius")
    print()
    print("OK, radius is ", r)
    h = float(input("Enter the height"))
    RNUM = float(r) ** 2
    Volume = 1/3 * math.pi * RNUM * h
    print("Volume is ", Volume)
    curved_floor = math.pi * RNUM * h
    print("Area of curved floor is ", curved_floor)
elif ( t == "ROOT OF A NUMBER") :
    number = int(input("Enter your number :"))
    power = int(input("Enter the power"))
    result = number ** power
    print(number,"^",power,"  =  ",result)
else :
    print("Please enter only valid shape in CAPITAL form.")

print("Thank you for using this calculator")
print("This calculator is created by Ahon")
