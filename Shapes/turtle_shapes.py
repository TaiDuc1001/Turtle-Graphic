import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
color1s = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', '#FFCC66', '#339999']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
so_canh = 4
goc = 360/so_canh + 1
for x in range(720):
	t.pencolor(color1s[x%so_canh])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(int(goc))