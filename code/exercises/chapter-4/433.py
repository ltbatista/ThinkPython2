import turtle

def polygon(t, length, n):
    for i in range(n):
        t.fd(50)
        t.lt(360/n)
    turtle.mainloop()

bob = turtle.Turtle()
polygon(bob, 100, 7)
