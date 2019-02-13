import math

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

# Line function
def f(x, angle, c) :
	m = round(math.tan(math.radians(angle)), 3)
	
	return round(m * x  +  c, 3) 

# Calc diagonal length
def diagonal_length(width, length):

	return round(math.sqrt(width**2 + length**2))


# Calc Lp (length where "c" in the line equation will be taken)
# alpha and theta are in degree!
def el_p(alpha, theta, diagonal, diagonal_up):

	if theta > alpha :
		