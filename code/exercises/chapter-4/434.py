import turtle

def circle(t, r):
    for i in range(36):
        t.fd(r)
        t.lt(360/36)
    turtle.mainloop()

bob = turtle.Turtle()
circle(bob, 15)
