# soal latihan hal 120

#1
# f(x) = x^3 + 2x^2 + 10x -20 = 0
# x = 1.368808107
from math import pow, sqrt
from numerik import fixed_point_iteration

def g1(x):
	atas = 20 - 2 * x**2 - 10 * x
	print atas
	g = pow(atas,1.0/3)
	return g

def g2(x):
	return sqrt(-0.5 * ( x**3 + 10*x -20 ))

def g3(x):
	return (x**3 + 2 * x**2 - 20)/(-10.0)

def g4(x):
	return (20.0 - 10 * x) / (x**2 + 2*x)

def g5(x):
	return (20.0 - 2 * x**2) / (x**2 + 10.0)

def g6(x):
	return (20 - x**3) / (2 * x - 10)

def g7(x):
	return 20.0 / (x**2 + 2*x + 10)

fungsi_g = [ g3, g4, g5, g6, g7]
roots = []

for g in fungsi_g:
	x_awal = 1.368
	roots.append(fixed_point_iteration(g, x_awal, epsilon=1e-8))

for root in roots:
	print root
# fixed_point_iteration(g5, 1.0, 1e-6)