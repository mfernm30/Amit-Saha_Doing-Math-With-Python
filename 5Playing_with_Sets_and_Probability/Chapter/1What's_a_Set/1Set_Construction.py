from sympy import FiniteSet
from fractions import Fraction

# Set Construction
s = FiniteSet(2, 4, 6)
print("Set construction: ", s)

# Storing different types of numbers
s = FiniteSet(1, 1.5, Fraction(1, 5))
print("Set with different types of numbers: ", s)

# Obtain the cardinality
print("Cardinality: ", len(s))

# Checking Wether a Number Is in a Set
print("Is number 4 in my set?: ", 4 in s)

# Creating an Empty Set
s = FiniteSet()
print("Empty set: ", s)

# Creating Sets from List or Tuples
members = [1, 2, 3]
s = FiniteSet(*members)
print("Set created from a list: ", s)

# Set Repetition and Order
members = [1, 3, 2, 2]
s = FiniteSet(*members)
print("Set order: ", s)

# Check if sets are equal
s = FiniteSet(3, 4, 5)
t = FiniteSet(5, 4, 3)
print("Are this 2 sets equal?: ", s == t)
