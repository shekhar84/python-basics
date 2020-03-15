# Boolean Expression True and false

day = "Monday"
temperature = 30
raining = True

if (day == "Saturday" and temperature > 27) and not raining:
    print("Go swimming")
else:
    print("Learn python")

# Truthy Values
if 1:
    print("True")
else:
    print("false")

name = input ("Please enter your name: ")
#if name:
if name != "":
    print("hello, {0}".format(name))
else:
    print("You don't have any name")
