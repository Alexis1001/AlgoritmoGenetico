import scipy as sp
import matplotlib.pylab as plt

for i in range(5):
    t = sp.linspace(0, 1, 100)

    plt.title("hola mi nueva graficas")
    plt.ylabel("calculadon esto perro ")
    plt.plot(t, t**2)
    plt.plot(t,t*2)
    plt.show()