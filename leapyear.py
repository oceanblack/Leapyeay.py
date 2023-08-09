year = int(input("which year do you want to check ?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("not a leap YEAR.")
    else:
      print("Leap year.")
else: 
   print(" not a leap year.")

##Check if the number is evenly divisible by 4, if not then it is not a leap year.

## If it is then check if it is evenly divisible by 100, if not then it is a leap year.

#If it is then check if it is evenly divisible by 400, if it is then it a leap year.

#If it is not then it is not a leap year.