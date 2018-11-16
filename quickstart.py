import graph_tool.all as gt
g = gt.Graph()

v0_g = g.add_vertex()
v1_g = g.add_vertex()
e0_g = g.add_edge(v0_g,v1_g)

g1 = gt.Graph(g) #this is a deep copy, so any further changes to g will not affect g1
v2_g = g.add_vertex()
e2_g = g.add_edge(v0_g,v2_g)
gt.graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200,200), output="two-nodes.png")
gt.graph_draw(g1, vertex_text=g1.vertex_index, vertex_font_size=18, output_size=(200,200), output="two-nodesg2.png")

for vertex in g.vertices():
	print(vertex, vertex.out_degree(), vertex.in_degree()) #this is slow as loops are performed in pure python, fastest method is below

print(g.get_vertices())
print(g.get_out_degrees(g.get_vertices()))
print(g.get_in_degrees(g.get_vertices()))
#edges = g.get_edges()
#print((edges[:,0] * edges[:,1]).sum())


