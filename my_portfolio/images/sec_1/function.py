import turtle as t
t.speed(6)
t.pensize(2)

def shape(side , angle): #fn definition
    for i in range(angle):
        t.fd(side)
        t.lt(360/angle)
        i=i+1

shape(100,4) #fn call
t.penup()
t.goto(150,150) #cordinates
t.pendown()
shape(100,6) #fn call
t.penup()
t.goto(-150,-150)
t.pendown()
shape(100,5) #fn call

t.done()