import numpy as np
import math
import matplotlib.pyplot as plt

# \sum_{i=0}^{108} (-1)^{108-i} \left(\begin{array}{c}108 \\ j\end{array}\right) {(\frac{i}{108})}^n
# show the exact number n to have 95% chance of getting all 108 coupons

def coupon(n):
    sum = 0
    for i in range(109):
        sum += (-1)**(108-i) * math.comb(108, i) * (i/108)**n
    return sum

# x: 200-1000
x = np.linspace(200, 1000, 1000)
y = [coupon(n) for n in x]

plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('Probability of getting all 108 coupons')
plt.title('Coupon Collector Problem')

# show the exact number n to have 95% chance of getting all 108 coupons in the graph
plt.axhline(y=0.95, color='r', linestyle='--')
plt.text(200, 0.95, '95%', color='r')

for i in range(200, 1000):
    if coupon(i) >= 0.95:
        plt.text(i, 0.95, str(i))
        plt.axvline(x=i, color='r', linestyle='--')
        break

plt.show()