import turtle

def arc(t, r, angle):
    for i in range(36):
        t.fd(r)
        t.lt(angle/36)
    turtle.mainloop()

bob = turtle.Turtle()
arc(bob, 3, 360)
