import turtle
from turtle import *
# Set initial position
penup ()
left (90)
fd (200)
pendown ()
right (90)
pensize(7)
def my_goto(x, y):
	penup()
	goto(x, y)
	pendown()

wn = turtle.Screen()
# wn.bgcolor('black')
# wn.setup(width=600, height=600)

# my_goto(0,200)
# my_goto(0,200)
# penup()
shape('turtle')
# flower base
fillcolor ("red")
begin_fill ()
circle (10,180)
circle (25,110)
left (50)
circle (60,45)
circle (20,170)
right (24)
fd (30)
left (10)
circle (30,110)
fd (20)
left (40)
circle (90,70)
circle (30,150)
right (30)
fd (15)
circle (80,90)
left (15)
fd (45)
right (165)
fd (20)
left (155)
circle (150,80)
left (50)
circle (150,90)
end_fill ()

# Petal 1
left (150)
circle (-90,70)
left (20)
circle (75,105)
setheading (60)
circle (80,98)
circle (-90,40)

# Petal 2
left (180)
circle (90,40)
circle (-80,98)
setheading (-83)

print(heading())
print(pos())
# pencolor('#21AF4B')
pensize(9)
# turtle.pensize(4)
# turtle.penup()
# turtle.goto(-1.23, -7.86)
# turtle.pendown()
# turtle.fd(30)


# my_goto()
# Leaves 1

fd (30)
left (90)
fd (25)
left (45)
fillcolor ("green")
begin_fill ()
circle (-80,90)
right (90)
circle (-80,90)
end_fill ()
right (135)
fd (60)
left (180)
fd (85)
left (90)
fd (80)

# Leaves 2
right (90)
right (45)
fillcolor ("green")
begin_fill ()
circle (80,90)
left (90)
circle (80,90)
end_fill ()
left (135)
fd (60)
left (180)
fd (60)
right (90)
circle (200,60)
my_goto(-270,-60)
write('Happy 20 / 11', font=("Bradley Hand ITC", 30, "bold"))

done()
