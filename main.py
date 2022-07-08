from ellipticCurve import Ell_Curve
from curve_point import Projective_Point
from xor import Cryptosystem

x, y = Ell_Curve.find_point()
P = Projective_Point(x, y)

Alice = Cryptosystem(Ell_Curve, P)
Bob = Cryptosystem(Ell_Curve, P)

_, Q_A = Alice.extract_keys()
_, Q_B = Bob.extract_keys()

s_1 = Alice.share_secret(Q_B)
s_2 = Bob.share_secret(Q_A)

print('shared secret equality:', s_1 == s_2)
