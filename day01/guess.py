# Author:s0cket

_oldboy_age = 56
count = 0

while count < 3:
    oldboy_age = int(input("oldboy_age:"))


    if oldboy_age == _oldboy_age:
        print("yes,you got it...")
        break
    elif oldboy_age>_oldboy_age:
        print("think smaller...")
    else:
        print("think bigger")
    count += 1
    if count == 3:
        continue_confirm = input("do you want to keep guessing...?")
        if continue_confirm != "n":
            count = 0
'''   
else:
    print("you have tried many times...fuck off")
'''

# for循环
# for i in range(0, 10, 1):
#     print("loop", i)