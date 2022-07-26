# this finds out the maximum power of n before the value exceeds 1000
from pickle import APPEND


n = 2 # could be any number
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
print(power)

