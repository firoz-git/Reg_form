import turtle as t
t.speed(0)
t.pensize(3)
t.color("red")
for i in range(60):
    for i in range(4):
        t.fd(200)
        t.lt(90)
    t.lt(6)
t.penup()

t.fd(500)

t.pendown()
for i in range(300):
    for i in range(6):
        t.fd(100)
        t.lt(60)
    t.lt(7)
t.done()

