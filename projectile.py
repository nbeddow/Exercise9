import math
import cmath

#version 1 of solution
# g=9.81
# y0=1
# x=0.5
# theta=80*(math.pi/180)
# v0=44
#
# print(math.pow(g,2))
# print(math.tan(theta))
# print(2*(math.pow(v0*math.cos(theta),2)))
#
# print((float(y0+x*(math.tan(theta))))-(g*(math.pow(x,2)))/(2*(math.pow(v0*math.cos(theta),2))))

#version 2 of solution with inputted variables

g=9.81
y0=float(input("please enter height of barrel: "))
x=float(input("please enter horizontal distance: "))
v0=float(input("please enter initial velocity: "))
elevation=float(input("please enter angle of elevation: "))
theta=elevation*(math.pi/180)

y=((y0+x*(math.tan(theta))))-(g*(math.pow(x,2)))/(2*(math.pow(v0*math.cos(theta),2)))
print("Height of projectile: ", round(y,2), "m")

#version 3 of solution with limits to input

