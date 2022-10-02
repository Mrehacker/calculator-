##---- AUTHOR=SUJAL------------##

##----PROJECT=CALCULATOR-------##

number1=float(input ("enter your first number :"))

	number2=float(input("enter your second number :"))

	

operation=input ("enter your operation :")

#......................calculation...................#

number3= number1 + number2

number4= number1 - number2

number5= number1 * number2

number6= number1 / number2 

number7= number1 ** number2

number8= number1 * number2 / 100

number9= number1 ** 0.5

number10= number1 ** 0.33333333333333333333333333

 #.................... operation.....................#

if operation=="+" :

    

    print("The sum =", number3)

    

elif operation=="/" :

    

    print("The sum =", number6)

    

    

elif operation=="-" :

    

   print("The sum =", number4)

elif operation=="*" :

    

    print("The sum =", number5)

        

elif operation=="**" :

    

    print("The quabe =", number7)

elif operation=="%" :

    

    print("The sum in presenteg(%) =", number8)

elif operation=="√" :

    

    print("The square root =", number9)

elif operation=="3√" :

    

    print("The quabe root =", number10)

    




