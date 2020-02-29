name = input("please enter your name:")
age = int(input("how old are you, {0}?".format(name)))
print(name, f"age is {age}")

# if age>=18:
#     print(name, " are old enough to vote")
#     print(name, "please place your vote at X box")
# else:
#     print(name, "please come back in {0} years".format(18-age))
if age<18:
    print(name, " are not old enough to vote")
    print(name, "please come back in {0} years".format(18-age))
elif age == 900:
    print(name, " are you still alive?")
else:
    print(name, " are old enough to vote")
    print(name, "please place your vote at X box")
