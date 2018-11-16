import numpy as np
from gym import spaces
from graph_tool.all import *

md = spaces.MultiDiscrete([ 5, 2, 2 ])
for i in range(10):
  print(md.sample())

print(md.contains(np.array([4, 1, 0], dtype=np.int32))) # False
print(md.contains(np.array([-1, 0, 0], dtype=np.int32)))

new = spaces.MultiDiscrete(np.full((10,10),2))
print(np.asarray(np.full((10,10),2)))
print(new.sample())

g = Graph()
g.set_fast_edge_removal(True)
number_input_nodes = 3
total_services = 10
inputServices = g.add_vertex(number_input_nodes)
otherServices = g.add_vertex(total_services - number_input_nodes)
adj = adjacency(g).toarray().astype(int)
print(adj)
print(new.sample())
print(new.contains(adj))
#for i in range(10):
#    print(new.sample())
