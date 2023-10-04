x = 10
name = "Samuel"
x = True
a = b = c = 1
a, b = 2, True
(a, b) = (2, True)
print(x)

x = "Hello world"
print(len(x))
print(x + "!!!")
print(x*2)
# [start:end(escluso):step] 0-based
print(x[0:5])
print(x[6:])
print(x[:5])
print(x[::2])
print(x[::-1])
print("Hello" in x)
print("Hello" not in x)

x = [1, 2, 3, 4, 5]
print(len(x))
x.append(6)
print(x)
x.insert(0,0)
print(x)
x.remove(0)
print(x)
x.pop()
print(x)
print(1 in x)
print(x[0:3])
print(x[3:])
print(x[::2])
print(x[::-1])
print(x + [6, 7, 8])
print(x*2)

x = [5, 3, 1, 4, 2]
x.sort()
print(x)
x.reverse()
y = x.copy()
print(y)
x.clear()
print(x)
print(y.index(3)) #0-based
y.extend([6,7,8])
print(y)
print(y.pop())
print(y)

#list comprehension
x = [1,2,3,4,5]

y = [i*2 for i in x]
print(y)
z = [i*2 for i in x if i % 2 == 0]
print(z)
pairs = [[i,j] for i in x for j in x]
print(pairs)

#tuples
x = (1,2,3,4,5)
print(x[0])
print(x[-1])

#dictionary
x = {"a" : 1, "b": 2, "c" : 3}
print(x["a"])
print(x["b"])
print(x.keys())
print(x.values())
print(x.items())
print(x.get("a"))
print(x.get("d"))
# x.get("...", default value if "..." not belongs on x)
print(x.get("a", 5))
print(x.get("d", 4))
x.update({"d" : 4})
print(x)

x = 5
oddity = "odd" if x % 2 == 1 else "even"
print(oddity)
if(x % 2 == 1):
    oddity = "odd"
else:
    oddity = "even"
print(oddity)

x = 5
while x > 0:
    print(x)
    x -= 1

# generates a sequence of numbers [0...4]
for i in range(5):
    print(i)

# break = used to exit a loop
# continue = used to skip the current iteration of a loop
# pass = is used to do nothing

#def add(x, y = 2):
#    return x + y

#print(add(1,3))
#print(add(1))

# *args -> non-keyworded, variable lenght argument-list
# **kwargs -> keyworded, '' '' ''
#def add(*args):
#    return sum(args)

#def add(**kwargs):
#    return sum(kwargs.values())

#print(add(1,2,3,4,5))
#print(add(a = 1, b = 2, c = 3))

add = lambda x, y: x + y

print(add(1,2))

import math
import numpy as np

print(math.sqrt(4))
print(np.sqrt(4))
