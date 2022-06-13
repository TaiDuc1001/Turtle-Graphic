from turtle import *
import turtle
wn = turtle.Screen()
# tur = Turtle()
heigth_win = 650
hwidth_win = 700
wn.setup(height = 400, width = 600)

def heart():
	my_goto(0, -70)
	pensize(width = 5)
	fillcolor('#e70010')
	begin_fill()
	seth(125)
	fd(100)
	circle(-35, 180)
	left(115)
	circle(-35, 180)
	goto(0,-70)
	end_fill()


def draw_circle():
	speed(6)
	pensize(width = 5)
	setheading(-90)
	fd(100)
	right(90)
	fillcolor('#66FFCC')
	begin_fill()
	circle(50)
	end_fill()

def my_goto(x, y):
	penup()
	goto(x, y)
	pendown()

def head():
	speed(6)
	pensize(width = 5)
	penup()
	circle(150,40)
	pendown()
	fillcolor('#00a0de')
	begin_fill()
	circle(150,280)
	end_fill()

def nose():
	my_goto(-10,158)
	seth(315)
	fillcolor('#e70010')
	begin_fill()
	circle(20)
	end_fill()

def scarf():
	fillcolor('#e70010')
	begin_fill()
	seth(0)
	fd(200)
	circle(-5, 90)
	fd(10)
	circle(-5, 90)
	fd(206)
	circle(-5, 90)
	fd(10)
	circle(-5, 90)
	end_fill()

def mouth():
	speed(1)
	my_goto(5, 148)
	seth(270)
	fd(100)
	seth(0)
	circle(120, 50)
	seth(230)
	circle(-120, 100)


	# pensize(width = 5)
	# fillcolor('#e70010')
	# begin_fill()
	# seth(125)
	# fd(100)
	# circle(-35, 180)
	# print(position())
	# left(125)
	# my_goto(0,0)
	# seth(55)
	# fd(100)
	# circle(35, 180)
	# end_fill()



# penup()
# circle(150,40)
# pendown()

# draw_circle()
# head()
# scarf()
# nose()
# mouth()
heart()
# star()
my_goto(50, -170)
speed(3)
write('Phan Tai Duc', font=("Bradley Hand ITC", 30, "bold"))
mainloop()


# penup()
# tur.circle(150, 40)
# tur.pendown()
# tur.fillcolor('#00a0de')
# tur.begin_fill()
# tur.circle(150, 280)
# tur.end_fill()


















































