from numerik import fixed_point_iteration

def g(x):
	return 2.0/x

fixed_point_iteration(g, 1.2, epsilon=1e-6)