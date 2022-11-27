from sympy import FiniteSet

space = FiniteSet(1, 2, 3, 4, 5, 6)
eventA = FiniteSet(2, 3, 5)
eventB = FiniteSet(1, 3, 5)
intersectAB = eventA.intersect(eventB)
probability = len(intersectAB)/len(space)

print('Sample space: {0}'.format(space))
print('Event A: {0}'.format(eventA))
print('Event B: {0}'.format(eventB))
print("Probability of event A(being prime number) and B(being odd number)", probability)