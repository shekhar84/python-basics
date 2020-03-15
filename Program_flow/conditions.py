age = int(input("how old are you?" ))

#if age >=16 and age <= 65:
#if 16 <= age <= 65:
#using the range
if age in range(16,66):
    print("have a good day at work")
else:
    print("Enjoy your free time")
print("-" * 30)

if age < 16 or age > 65:
    print("Enjoy your free time")

