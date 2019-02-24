import math
import numpy
import matplotlib.pyplot as plt

# Slicing through a rectangular
# Note :
# 1. The direction normal to slice should be (0 < alpha < 90)
# 2. Width (B) < Length (L) of the rectangular

# Define the rectangular dimension
B = 20
L = 40

# Direction of slice (in DEGREE)
# The slice is perpendicular of this direction
THETA = 45


# Calculate ALPHA (angle of the rec diagonal)
alpha = math.degrees(math.atan(B/L))
print(alpha)


# Function definition

# Line function f(x)
def fx(x, angle, c) :
	m = round(math.tan(math.radians(angle)), 3)
	
	return round(m * x  +  c, 3) 

# Line function f(y)
def fy(y, angle, c) :
	m = round(math.tan(math.radians(angle)), 3)

	return round((y - c)/m, 3)

# Calc diagonal length
def diagonal_length(width, length):

	return round(math.sqrt(width**2 + length**2))


# Calc Lp (length where "c" in the line equation will be taken)
# alpha and theta are in degree!
def el_p(alpha, theta, diagonal):

	if theta > alpha :
		diagonal_up = diagonal * math.cos(math.radians(theta - alpha))

	elif theta < alpha :
		diagonal_up = diagonal * math.cos(math.radians(alpha - theta))

	else :
		diagonal_up == diagonal

	el_p = diagonal_up / math.cos(90 - math.radians(theta))

	return round(el_p, 3)


# Start program
dia_length = diagonal_length(B, L)

# Calculate Lp
Lp = el_p(alpha, THETA, dia_length)
print ("This is Lp = ", Lp)

# Calc properties for each slice 
nodes_list = []
x1 = 0
x2 = L
y3 = 0
y4 = B

for c in numpy.arange(0, Lp, round(Lp/100, 3)) :

	node_selected = []
	
	# Solve f(x), x = 0
	y1 = fx(x1, THETA + 90, c)
	if 0 <= y1 <= B :
		node_selected.append([x1, y1])

	# Solve f(x), x = L
	y2 = fx(x2, THETA + 90, c)
	if 0 <= y2 <= B :
		node_selected.append([x2, y2])

	# Solve f(y), y = 0
	x3 = fy(y3, THETA + 90, c)
	if 0 <= x3 <= L :
		node_selected.append([x3, y3])

	# Solve f(y), y = B
	x4 = fy(y4, THETA + 90, c)
	if 0 <= x4 <= L :
		node_selected.append([x4, y4])

	# Put all the selected nodes into a list
	nodes_list.append([c, node_selected])


#Check nodes coordinates
print(*nodes_list, sep="\n")


# Check line formula
# x_list = []
# y_list = []
# for xi in range(0, 40) :
# 	x_list.append(xi)
# 	y_list.append(fx(xi, THETA + 90, 10))

# plt.figure(1)
# plt.plot(x_list, y_list)
# plt.show()



