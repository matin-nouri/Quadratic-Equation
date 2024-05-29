import matplotlib.pyplot as plt 
import numpy as np
print("ax2 + bx + c = 0")

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

Δ = b**2 - 4*a*c

x = 0

if Δ < 0:
    print("Equaption does not have any result!")
    exit(0)

if Δ == 0:
    x = (-1 * b) / (2*a)
    plt.scatter(x,0, c = "Red")

if Δ > 0:
    x1 = ((-1 * b) + Δ**(1/2)) / (2*a)
    x2 = ((-1 * b) - Δ**(1/2)) / (2*a)
    x = [x1,x2]
    y = [0,0]
    plt.scatter(x,y,c = "Red")

plt.show()