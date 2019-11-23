from Vector import *
from Complex import *

def main():
	v = Vector3f(1,2,2)
	u = Vector3f(3,4,1)
	z = Complex(1,1)
	w = expi(0)
	a = dot_product(v,u)
	x = add_vector(v,u)
	b = add_complex(z,w)
	print(b)
	print(x.getVector())
if __name__ == "__main__":
	main()