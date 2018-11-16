from graph_tool.all import *
import numpy as np
g = Graph()
servicelist = g.add_vertex(7)
e1 = g.add_edge(g.vertex(2),g.vertex(5))
edges = g.add_edge_list([[0,1],[2,3],[4,6]])
graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(1000,1000), output="services.png")
adjacency = adjacency(g)
print(adjacency)
print(adjacency.toarray())
print(is_DAG(g))
rand = price_network(20)
graph_draw(rand, vertex_text=rand.vertex_index, vertex_font_size=18, output_size=(1000,1000), output="rand.png")
print(is_DAG(rand))

