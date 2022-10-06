try:
    x = int(input("Enter a number: "))
    y = 1/0
    print(y)
except ZeroDivisionError:
    print("You can't divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print ("Oh dear, something went wrong...")
print("THE END.")