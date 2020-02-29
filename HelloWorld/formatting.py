for i in range(1,13):
    print("No. of {0:2} squared is {1:3} and cubed is {2:3}".format(i, i ** 2, i **3))
print()
for i in range(1,13):
    print("No. of {0:2} squared is {1:<3} and cubed is {2:^3}".format(i, i ** 2, i **3))




print("Pi is approximately {}".format(22/7))
print("Pi is approximately {0:<10f}".format(22/7))
print("Pi is approximately {0:<10.22f}".format(22/7))
print("Pi is approximately {0:<12.22f}".format(22/7))
print(f"Pi is approximately {22 / 7:12.50f}")

age =24

print("shekhar age is " + f"{age}")
