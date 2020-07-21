import turtle
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n =  int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle =  float(angle) / n
    polyline(t, n, step_length, step_angle)
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

bob = turtle.Turtle()

## chamar a funcao
turtle.mainloop()


    
