from turtle import *
import turtle
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=500, height=500)

r_dot = 9

def my_goto(x, y):
	penup()
	goto(x, y)
	pendown()

def top_point():
	reset()
	setworldcoordinates(0,1571,1571,0)
	pencolor('white')
	pensize(7)



	my_goto(470,503)
	goto(501,422)
	goto(1090,422)
	goto(1117,503)

	my_goto(721,422)
	goto(795,221)
	goto(874,422)

	my_goto(1249,899)
	goto(1281,951)
	goto(795,1312)
	goto(319,973)
	goto(385,756)

	my_goto(441,1163)
	goto(415,1247)
	goto(1175,1247)
	goto(1146,1163)

	pensize(3)

	my_goto(328,704)
	dot(r_dot,'white')
	my_goto(345,724)
	dot(r_dot,'white')
	goto(561,608)
	dot(r_dot,'white')
	goto(561,657)  #4
	dot(r_dot,'white')
	my_goto(492,720) #6
	dot(r_dot,'white')


	goto(561,720)
	dot(r_dot,'white')
	goto(749,869)
	dot(r_dot,'white')
	goto(749,526)
	dot(r_dot,'white')
	goto(749,476)
	dot(r_dot,'white')
	goto(328,704)

	my_goto(561,657)
	goto(561,720)

	my_goto(725,1168)
	dot(r_dot,'white')
	goto(725,1003)
	dot(r_dot,'white')
	goto(665,799)
	dot(r_dot,'white')

	my_goto(749,869)
	goto(749,1101)
	dot(r_dot,'white')
	goto(749,1165)
	dot(r_dot,'white')

	my_goto(795,1165)
	dot(r_dot,'white')
	goto(795,688)
	dot(r_dot,'white')
	goto(795,688)
	dot(r_dot,'white')
	goto(795,526)
	dot(r_dot,'white')

	my_goto(749,526)
	goto(667,559)
	dot(r_dot,'white')
	goto(647,533)

	my_goto(749,526)
	goto(667,621)
	dot(r_dot,'white')
	goto(614,550)

	my_goto(749,526)
	goto(667,589)
	dot(r_dot,'white')
	goto(629,541)

	my_goto(611,654)
	dot(r_dot,'white')
	goto(667,656)
	dot(r_dot,'white')
	goto(749,658)

	my_goto(611,654)
	goto(667,687)
	dot(r_dot,'white')
	goto(749,691)

	my_goto(611,654)
	goto(667,719)
	dot(r_dot,'white')
	goto(749,720)

	my_goto(667,756)
	dot(r_dot,'white')

	my_goto(795,1003)
	dot(r_dot,'white')

	my_goto(795,1165)
	goto(985,1079)
	dot(r_dot,'white')

	my_goto(821,1153)
	goto(819,689)
	goto(877,608)
	dot(r_dot,'white')

	my_goto(855,1139)
	dot(r_dot,'white')
	goto(853,1067)
	goto(904,1004)
	dot(r_dot,'white')
	goto(961,1089)

	my_goto(855,1139)
	goto(931,1045)

	# ================

	my_goto(878,574)
	dot(r_dot,'white')

	my_goto(878,653)
	dot(r_dot,'white')

	my_goto(878,688)
	dot(r_dot,'white')

	my_goto(919,688)
	dot(r_dot,'white')

	my_goto(919,650)
	dot(r_dot,'white')

	my_goto(919,610)
	dot(r_dot,'white')

	my_goto(919,573)
	dot(r_dot,'white')
	# ================


	my_goto(878,688)
	goto(853,723)
	goto(853,906)
	dot(r_dot,'white')
	goto(904,905)
	dot(r_dot,'white')
	my_goto(853,906)
	goto(853,1004)
	dot(r_dot,'white')
	goto(904,1004)
	dot(r_dot,'white')


	goto(902,722)
	goto(919,688)
	goto(1046,549)
	dot(r_dot,'white')
	goto(1126,580)
	goto(1201,608)
	dot(r_dot,'white')
	goto(1258,654)
	goto(1285,700)
	dot(r_dot,'white')
	goto(1286,786)
	dot(r_dot,'white')
	goto(1239,857)
	dot(r_dot,'white')
	goto(1162,904)
	goto(1072,905)
	dot(r_dot,'white')


	my_goto(795,526)
	goto(931,529)
	goto(1046,549)


	my_goto(961,644)
	dot(r_dot,'white')
	goto(1048,662)
	dot(r_dot,'white')
	goto(1077,639)
	goto(1237,636)
	goto(1237,783)
	dot(r_dot,'white')
	goto(1193,858)
	goto(1142,892)
	goto(1072,905)
	my_goto(1262,822)
	goto(1259,701)
	goto(1237,665)
	goto(1048,662)

	my_goto(961,644)
	goto(1048,607)
	dot(r_dot,'white')
	goto(1074,583)
	goto(1126,580)
	my_goto(1048,607)
	goto(1201,608)


	# =========================
	fillcolor('white')
	begin_fill()
	my_goto(1041,739)
	goto(1117,739)
	goto(1117,813)
	goto(1041,813)
	goto(1041,739)
	end_fill()

	my_goto(1046,727)
	goto(1046,823)
	my_goto(1060,727)
	goto(1060,823)
	my_goto(1074,727)
	goto(1074,823)
	my_goto(1086,727)
	goto(1086,823)
	my_goto(1099,727)
	goto(1099,823)
	my_goto(1112,727)
	goto(1112,823)

	my_goto(1032,743)
	goto(1128,743)
	my_goto(1032,757)
	goto(1128,757)
	my_goto(1032,769)
	goto(1128,769)
	my_goto(1032,783)
	goto(1128,783)
	my_goto(1032,796)
	goto(1128,796)
	my_goto(1032,808)
	goto(1128,808)
	# ===============================

	my_goto(867, 1535)
	speed(3)
	write('Tp.Robotics ', font=("Bradley Hand ITC", 28, "bold"))


top_point()
mainloop()




# Cre: Phan Tài Đức C9