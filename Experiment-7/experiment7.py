class A:
    def one(self):
        a = 2
        print(a)


# single level
class B(A):
    def two(self):
        b = 3
        print(b)


obj = B()
obj.one()
obj.two()


# multiple
class G:
    def seven(self):
        g = 7
        print(g)


class C(G, A):
    def three(self):
        c = 10
        print(c)


obj1 = C()
obj1.one()
obj1.seven()
obj1.three()


# hybrid
class D(A):
    def four(self):
        d = 1
        print(d)


class E(B, D):
    def five(self):
        e = 12
        print(e)


obj2 = E()
obj2.one()
obj2.two()
obj2.four()
obj2.five()


# multi-level
class F(A):
    def six(self):
        f = 34
        print(f)


obj3 = F()
obj3.one()
obj3.six()


# hierarchical
class H(A):
    def eight(self):
        h = 38
        print(h)


class I(B):
    def nine(self):
        i = 38
        print(i)


obj4 = H()
obj4.one()
obj4.eight()

obj5 = I()
obj5.one()
obj5.two()
obj5.nine()


# polymorphism
class J:
    def poly(self, a):
        return a + a


class K(J):
    def poly(self, a, b):
        print("one:", super().poly(a))
        return a - b


obj6 = K()
print("two:", obj6.poly(9, 7))
