from ellipticCurve import Ell_Curve

class Affine_Point:

    def __init__(self, x, y):

        self.ellipticCurve = Ell_Curve
        self.x = x % self.ellipticCurve.p
        self.y = y % self.ellipticCurve.p

        if not (self.y ** 2) % self.ellipticCurve.p == (self.x ** 3 + self.ellipticCurve.a * self.x + self.ellipticCurve.b) % self.ellipticCurve.p:
            raise Exception('Point is not on curve')


    def Affine_To_Projective_Point(self):

        return Projective_Point(self.x, self.y, 1)


class Projective_Point:

    def __init__(self, x, y, z = 1):

        self.ellipticCurve = Ell_Curve

        self.x = x % self.ellipticCurve.p
        self.y = y % self.ellipticCurve.p
        self.z = z % self.ellipticCurve.p

        if not (self.y ** 2 * self.z) % self.ellipticCurve.p == (self.x ** 3 + self.ellipticCurve.a * self.x * self.z ** 2 + self.ellipticCurve.b * self.z ** 3) % self.ellipticCurve.p:
            raise Exception('Point is not on curve')

    def Projective_To_Affine_Point(self):

        if self == Projective_Point(0, 1, 0) or self.z == 0:
            return 'O_E'

        U, U1 = 1, 0
        V, V1 = 0, 1

        while self.ellipticCurve.p:
            q = self.z // self.ellipticCurve.p
            U, U1 = U1, U - q * U1
            V, V1 = V1, V - q * V1
            self.z, self.ellipticCurve.p = self.ellipticCurve.p, self.z - q * self.ellipticCurve.p

        inverse_z = (U % self.ellipticCurve.p + self.ellipticCurve.p) % self.ellipticCurve.p

        aff_x = self.x * inverse_z
        aff_y = self.y * inverse_z

        return Affine_Point(aff_x, aff_y)

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y and self.z == other.z and self.ellipticCurve == other.ellipticCurve

    def __add__(self, other):

        if self == Projective_Point(0, 1, 0):

            return other
        if other == Projective_Point(0, 1, 0):

            return self

        U1 = other.y * self.z
        U2 = self.y * other.z
        V1 = other.x * self.z
        V2 = self.x * other.z

        if V1 == V2:
            if U1 != U2:
                return Projective_Point(0, 1, 0)
            else:
                return self.Point_Double(self.x, self.y, self.z)

        U = U1 - U2
        V = V1 - V2
        W = self.z * other.z
        A = U ** 2 * W - V ** 3 - 2 * V ** 2 * V2
        res_x = V * A
        res_y = U * (V ** 2 * V2 - A) - V ** 3 * U2
        res_z = V ** 3 * W

        return Projective_Point(res_x, res_y, res_z)

    def __mul__(self, k):

        bits = bin(k)
        res = Projective_Point(0, 1, 0)
        temp = self

        for i in range(0,len(bits) - 1):
            if bits[i] == 1:
                res += temp
            else:
                temp = temp.Point_Double()

        return res

    def Point_Double(self):

        if self.y == 0:
            return Projective_Point(0, 1, 0)

        if self == Projective_Point(0, 1, 0):
            return Projective_Point(0, 1, 0)

        W = self.ellipticCurve.a * self.z ** 2 + 3 * self.x ** 2
        S = self.y * self.z
        B = self.x * self.y * S
        H = W ** 2 - 8 * B

        x_1 = 2 * H * S
        y_1 = W * (4 * B - H) - 8 * self.y ** 2 * S ** 2
        z_1 = 8 * S ** 3

        return Projective_Point(x_1, y_1, z_1)