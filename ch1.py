def sqrt(num):
	return num ** (1 / 2)

def quad_roots(coeff1, coeff2, coeff3):
	root1 = -coeff2 + sqrt((coeff2 ** 2) - (4 * coeff1 * coeff3))
	root1 = root1 / (2 * coeff1)
	root2 = -coeff2 - sqrt((coeff2 ** 2) - (4 * coeff1 * coeff3))
	root2 = root2 / (2 * coeff1)
	return root1, root2

def print_add_many(num1, num2):
	for i in range(30):
		print(num1 + num2)