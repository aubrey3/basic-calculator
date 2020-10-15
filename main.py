digit1 = input("put your number in")
digit2 = input("put your other number in")
mtype = input("What function do you want to do")

if mtype == "+":
    print(digit1 + digit2)
elif mtype == "-":
    print(digit1 - digit2)
elif mtype == "/":
    print(digit1 / digit2)
elif mtype =="*":
    print(digit1 * digit2)
else:
    print("Your function is wrong do it again")
