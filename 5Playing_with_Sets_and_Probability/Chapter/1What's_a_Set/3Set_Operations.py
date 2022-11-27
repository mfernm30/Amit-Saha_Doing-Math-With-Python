from sympy import FiniteSet

# Union
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)

print("Union: ", s.union(t))

# Intersection
s = FiniteSet(1, 2)
t = FiniteSet(2, 3)

print("Intersection: ", s.intersect(t))

# Union and intersection multiple sets
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
u = FiniteSet(3, 5, 7)

print("Multiple set union: ", s.union(t).union(u))
print("Multiple set intersection:", s.intersect(t).intersect(u))

# Cartesian Product
s = FiniteSet(1, 2)
t = FiniteSet(3, 4)
p = s*t
print("Cartesian Product: ", p)
print("Elements of product set:")
for elem in p:
    print(elem)

# Check cardinality of product sets
print("Is len(p) == len(s)*len(t): ", len(p) == len(s)*len(t))

# Cartesian product n times
s = FiniteSet(1, 2)
p = s**3

print("N times Cartesian product: ", p)
print("Elements of product set:")
for elem in p:
    print(elem)