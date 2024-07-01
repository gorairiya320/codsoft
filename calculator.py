first_number=int(input("Enter first number:-\n"))
second_number=int(input("Enter second number:-\n"))

while True:
    print('''Choose any operator for the operation:-
    1.'+' for summetion 
    2.'-' for subtraction 
    3.'*' for multiplication
    4.'/' for division
    5.'pow' for power operation
    6.'%' for modular operation
    7.'E' foe exit!''' )

    choose_operator=input("Choose any:-  [+,-,*,/,pow,%,E]\n")
    print( "You are choosing:",choose_operator)

    if choose_operator=="+":
        sum=first_number+second_number
        print(f"Summation of two number is {first_number}+{second_number}={sum}\n")
    elif choose_operator=="-":
        sub=first_number-second_number
        print(f"Subtract of two number is {first_number}-{second_number}={sub}\n")
    elif choose_operator=="*":
        mul=first_number*second_number
        print(f"Multiplication of two number is {first_number}*{second_number}={mul}\n")
    elif choose_operator=="/":
        div=first_number/second_number
        print(f"Division of two number is {first_number}/{second_number}={div}\n")
    elif choose_operator=="pow":
        pow=first_number**second_number
        print(f"{first_number} to the power {second_number} is: {pow}\n")
    elif choose_operator=="%":
        mod=first_number%second_number
        print(f"Remainder value  is {first_number}%{second_number}={mod}\n")
    elif choose_operator=="E":
        print("Thank you for using this calculator!\n")
        break
    else:
        print("Invalid Operator!")



    


