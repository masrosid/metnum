import math

def fixed_point_iteration(g, x, epsilon = 1e-5, N=30):
	"""
	Assume f is a function of x, f(x) and x = g(x) is the fixed point (see Metode Numerik by Rinaldi Munir)
	x : first guess for the root
	epsilon : error
	N : maximum number of iteration

	This function will return the root of the polynomial f(x).

	"""
	root_before = x
	root = g(x)
	i = 0
	print 'Hampiran akar pada iterasi ke-%d adalah %.6f, dengan galat: %.6f' % (i+1, root, abs(root - root_before))
	while abs(root - root_before) >= epsilon and i < N -1:
		root_before = root
		root = g(root)
		i += 1
		print 'Hampiran akar pada iterasi ke-%d adalah %.6f, dengan galat: %.6f' % (i+1, root, abs(root - root_before))

	if i > N:
		print "Fungsi divergen!"
		return None
	else:
		print 'Hampiran akar %.6f' % (root)
		return root


def g1(x):
	return math.sqrt(2*x + 3)

def g2(x):
	return 3.0 / (x -2)

def g3(x):
	return (x**2 - 3)/2.0

def prod(number_list):
	'''Return the product of all elements (int)'''
	sum = 1
	for i in number_list:
		sum *= i

	return sum

def isNumberDivisible(number, number_list):
	for i in number_list:
		if number % i != 0:
			return False
	return True

def find_prime(n):
    """
    Return a list of prime number below n
    Usage:
    find_prime(10)
    >>> [2, 3, 5, 7]
    """
    primelist = []
    for i in range(n + 1):
        primelist.append(True)
         
    primelist[0] = primelist[1] = False
     
    batas = int(math.sqrt(n) + 1)
    for i in range(2, batas + 1):
        if primelist[i]:
            for j in range(i*i, n + 1,i):
                if (j % i == 0):
                    primelist[j] = False
                 
    myprime = []
    for i in xrange(n + 1):
        if primelist[i]:
            myprime.append(i)
     
    return myprime


def gcd(a, b):
	'''
	Return the greatest common divisor
	'''
	if b > a:
		return gcd(b,a)
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
	return a*b/gcd(a, b)


def main():
	#print fixed_point_iteration(g1, 4, epsilon=1e-6)
	#print fixed_point_iteration(g2, 4, epsilon=1e-6)
	#print fixed_point_iteration(g3, 4, epsilon=1e-6)
	pass


if __name__ == '__main__':
	main()