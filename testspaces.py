import numpy as np
from gym import spaces

md = spaces.MultiDiscrete([ 5, 2, 2 ])
for i in range(10):
  print(md.sample())

print(md.contains(np.array([4, 1, 0], dtype=np.int32))) # False
print(md.contains(np.array([-1, 0, 0], dtype=np.int32)))

new = spaces.MultiDiscrete(np.full((10,10),2))
print(np.asarray(np.full((10,10),2)))
print(new.sample())
#for i in range(10):
#    print(new.sample())
