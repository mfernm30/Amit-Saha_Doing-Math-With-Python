from sympy import FiniteSet

# is_subset function
s = FiniteSet(1)
t = FiniteSet(1, 2)

print("Is set S a subset from T?: ", s.is_subset(t))

# Empty sets are subsets of every set
s = FiniteSet()
t = FiniteSet()
print("Is set S a subset from S?: ", s.is_subset(s))
print("Is set S a subset from empty subset T?: ", s.is_subset(t))

# is_superset() function
s = FiniteSet(1)
t = FiniteSet(1, 2)
print("Is set S a superset from T?: ", s.is_superset(t))
print("Is set T a superset from subset S?: ", t.is_superset(s))

# Powersets
s = FiniteSet(1, 2, 3)
ps = s.powerset()
print(ps)
print("Cardinality of powerset PS: ", len(ps))

# is_proper_subset function
s = FiniteSet(1, 2, 3)
t = FiniteSet(1, 2, 3)
t1 = FiniteSet(1, 2, 3, 4)
print("Is set S a proper subset of set T?: ", s.is_proper_subset(t))
print("Is set S a proper subset of set T?: ", s.is_proper_subset(t1))
