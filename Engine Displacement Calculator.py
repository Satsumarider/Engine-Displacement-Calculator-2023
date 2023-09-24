#Imports mathematics to allow pi to be used.
import math
#Defines pi (in it's entirety) so that it can be used to calculate the volume of the cylinders.
pi = math.pi
#Displays the title of the program.
print ("Engine Displacement Calculator 2023 ")
#Asks user to input engine bore size.
print ("How wide is the engine's bore in milimetres? ")
#Stores bore size in a variable.
bore = input()
#Asks user to input engine stroke length.
print ("What is the engine's stroke in milimetres? ")
#Stores stroke length in a variable.
stroke = input()
#Asks user to input number of cylinders.
print ("How many cylinders does the engine have? ")
#Stores number of cylinders in a variable.
numberOfCylinders = input()
#Calculates engine capacity in cubic centimetres, involving pi and indices.
displacement = ((float(stroke) * 0.1) * pi * (((float(bore) * 0.1) / 2) ** 2) * int(numberOfCylinders))
#Converts cubic centimetres into cubic inches.
cui = displacement / 16.387
#Converts cubic centimetres into litres.
litre = displacement * 0.001
#Uses 'an' as the connector to refer to an engine who's displacement starts with a vowel.
if 8 <= displacement < 9 or 11 <= displacement < 12 or 18 <= displacement < 19 or 80 <= displacement < 90 or 800 <= displacement < 900 or 8000 <= displacement < 9000 or 11000 <= displacement < 12000 or 18000 <= displacement < 19000 or 80000 <= displacement < 90000:
    print ("This is an", round(displacement), "cc engine.")
    print (round(displacement), "cc ≈", "%.1f" % litre, "L")
    print ("%.1f" % litre, "L ≈", round(cui), "cui")
#Uses 'a' as the connector to refer to an engine who's displacement starts with a consonant.
else:
    print ("This is a", round(displacement), "cc engine.")
    print (round(displacement), "cc ≈", "%.1f" % litre, "L")
    print ("%.1f" % litre, "L ≈", round(cui), "cui")