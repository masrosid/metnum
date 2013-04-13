from pylab import plot, xlabel, ylabel, title, legend, axis, grid, savefig, show, sin, cos
from numpy import linspace, pi

x = linspace(-2 * pi, 2*pi, 1e4)

y1 = sin(x)
y2 = cos(x)
y3 = sin(x) + cos(x)
y4 = sin(x) - cos(x)
y5 = cos(x) - sin(x)

plot(x, y1, x, y2, x, y3, x, y4, x, y5)
legend(['$\sin{x}$', '$\cos{x}$', '$\sin{x} + \cos{x}$', '$\sin{x} - \cos{x}$', '$\cos{x} - \sin{x}$'], loc='best')
xlabel('x')
ylabel('y')
title('Grafik Fungsi sin, cos dll')
grid()
axis('tight')
savefig('image.png')
savefig('image.pdf')
savefig('image.jpg')

show()