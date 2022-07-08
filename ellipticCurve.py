p = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
a = -3
b = 1093849038073734274511112390766805569936207598951683748994586394495953116150735016013708737573759623248592132296706313309438452531591012912142327488478985984
n = 6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449

import random

class EllipticCurve:
	def __init__(self, a, b, p, n):
		self.a = a
		self.b = b
		self.p = p
		self.n = n

	def __eq__(self, other):

		return (self.a, self.b, self.p) == (other.a, other.b, other.p)

	def find_point(self):
		self.x, self.y, self.z = 1, 1, 1

		while not (self.y ** 2 * self.z) % self.p == (self.x ** 3 + self.a * self.x * self.z ** 2 + self.b * self.z ** 3) % self.p:
			self.x = random.randint(1, self.p) ** 2 % self.p
			y_2 = (self.x ** 3 + self.a * self.x + self.b) % self.p
			self.y = pow(y_2, (self.p - 3) // 4 + 1, self.p)

		return self.x, self.y

Ell_Curve = EllipticCurve(a, b, p, n)
