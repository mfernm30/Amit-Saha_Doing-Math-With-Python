import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 2, 3]

fig = plt.figure()
ax = plt.axes()

'''
Besides manually creating Figure and Axes objects, you can use two
different functions in the pyplot module to get a reference to the current
Figure and Axes objects (gcf() and gca())
'''
figure_copy = plt.gcf()
axes_copy = plt.gca()

plt.plot(x, y)
plt.show()
