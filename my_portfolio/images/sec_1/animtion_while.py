from turtle import *
from random import randint
colormode(255) #help to add rgb
bgcolor("black")
speed(0)

x=1
while x<500:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    
    color (r,g,b)
    fd(x)
    rt(150.911) #angle changing will give better animations
    
    x=x+1

fd(200)
hideturtle()
done()