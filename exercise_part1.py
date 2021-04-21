"""Intro to Python - Part 1 - Hands-On Exercise."""
#Cambio en el archivo
#otro coment
#comentario en branch, comentario hecho en github
<<<<<<< HEAD
#hola
=======
#comentario 21/04/2021
>>>>>>> newfeature
import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print ("pi es de tipo: ", pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print (i)
if i < 50:
    print ("i menor 50")
else :
    print ("i mayor a 50")




# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit== "orange":
    print ("naranja")
elif picked_fruit== "strawberry":
    print ("rojo")
elif picked_fruit== "banana":
    print ("amarillo")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.


def mult(i,x):
    return (i*x)

# TODO: Now call the function a few times to calculate the following multiplications and print the results.

# 12 x 96

print (mult(12,96))

# 48 x 17
print (mult(48,17))

# 196523 x 87323
print (mult(196523,87323))
