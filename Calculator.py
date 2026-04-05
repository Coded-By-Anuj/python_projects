#Python mini project first
#Simple building a arithmatic calculator using python programming

try:
    int_1=int(input("Enter your first number :- "))
    int_2=int(input("Enter your second number :- "))

    sum=int_1+int_2
    print("The summation of the given two numbers will be :- ",str(sum))

    sub=int_1-int_2
    print("The substraction of the given two numbers will be :- ",str(sub))


    mul=int_1*int_2
    print("The multiplication of the given two numbers will be :- ",str(mul))


    div=int_1+int_2
    print("The division of the given two numbers will be :- ",str(div))


except ZeroDivisionError as msg:
    print("Zero division exception is caught :- ",msg)

except ValueError as msg:
    print("Value error Exception is caught :- ",msg)

except SyntaxError as msg:
    print("Syntax error Exception is caught :- ",msg)

except Exception:
    print("Exception is Caught..",msg)

else:
    print("<<Hey coders...No exception found in between Code...>>")

finally:
    print("This is the finally Block..\nYour Execution is successfully Executed..")
