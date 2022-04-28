#По двум заданным числам проверить является ли одно квадратом второго 
import os
numberOne = int(input("Input 1st Number: "))
numberTwo = int(input("Input 2nd Number: "))

if numberOne == numberTwo**2:
    print("1st number == 2nd number ^2")
elif numberTwo == numberOne**2:
    print("2nd number == 1st number ^2")
else:
    print("No quads in da house")