from math import *
import numpy as np
import matplotlib.pylab as plt


""" Calculating the area """
#d = 10.0			# diameter
#A = pi * d**2 / 4

#print "diameter =", d
#print "area = ", A

""" Greeting code """ 
#s = raw_input("What is your name?")
#print "HELLO", s

#x = int(raw_input("Input an integer"))
#y = float(raw_input("Input a float"))
#print x, y

""" Calculate area of a circle by inserting my own diamteter each step """
#d = float(raw_input("Diameter"))
#A = pi*d**2 / 4

#print "Area=", A

""" Calculate square root of numbers 0  to 1000 """

#i = 0
#while i<= 100:
#	print i,"\t\t" , sqrt(i)
#	i = i + 1  # can also be written like i +=  1
	
#print "READY!"

"""Endless loop, stop it like Ctrl - C"""

#i = 0
#while i<= 5:
#	print i 

""" Testing : if, elif, else """

#s = raw_input("Input your name: ")

#if s == "Ayanda":
#     print "HELLO ", s
 
""" else """    
#if s == "Ayanda":
	#print "HELLO ", s
#else:
#	print "HELLO unknown" 

""" elif """

#if s == "Ayanda":
#	print "HELL", s
#elif s == "Tom":
#	print "I'm so glad to see you ", s
#elif s == "Honey":
#	print "I didn't expect you", s
#else:
#	print "HELLO unknown"

""" functions definitions """
def area(b, h): 
	"""Calculates area of rectangle """
	A = b*h
	return A

def perimeter(b, h):
	""" Calculates perimeter of a rectangle """
	P = 2*(b+h)
	return P
	
#Main program using defined functions
width = 5
height = 3

print "Area = ", area(width, height)
print "Perimeter = ", perimeter(width, height)

""" A function can return more than one value """
					
def area_and_perimeter(b, h):
	A = b*h
	P = 2*(b+h)
	return A, P
	
#Main program using defined function

ar, per = area_and_perimeter(4,3)
#print ar
#print per

# Calculate 100 values for x and y without a for loop

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

#print x
#print y

# Calculate 500 values for x and y without a for loop

x1 = np.linspace(0, 10*np.pi, 500)
y1 = np.sin(x1)*np.exp(-x1/10)

#make a plot
plt.plot(x1, y1)
plt.show()
