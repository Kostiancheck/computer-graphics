import matplotlib.pyplot as plt
import numpy as np
import re

x = np.arange(-24, 24, 0.01)
y = np.abs(np.arctan(x))
# for i in range(len(y)):
#     y[i] = round(y[i], 2)

f = open('file_data.txt', 'w')

for i in range(len(x)):
    f.write(str(x[i]) + " " + str(y[i]) + "\n")

f.close

f = open('file_data.txt', 'r')
lines = f.readlines()
x = []
y = []

for line in lines:
    spl = re.split("\s", line)
    x.append(float(spl[0]))
    y.append(float(spl[1]))

print(x)
print(y)

line = plt.plot(x, y, lw=3)

plt.ylabel('f(x)=|arctg(x)|')
plt.axhline(y=np.pi / 2, color='r', linestyle='dashed')
plt.ylim(0, 2)
plt.yticks(np.arange(0, 2, 0.25))
plt.xticks(np.arange(-24, 23, 3))

plt.savefig('figure1.png')
plt.show()

f.close()
