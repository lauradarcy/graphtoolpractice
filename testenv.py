from graph_tool.all import *

g = Graph()
g.set_fast_edge_removal(True)
number_input_nodes = 3
total_services = 10
inputServices = g.add_vertex(number_input_nodes)
otherServices = g.add_vertex(total_services - number_input_nodes)
terminationService = g.add_vertex()

print(g.vertex(0) in otherServices)

adjacency_m = adjacency(g)
print(adjacency_m.toarray())
print(is_DAG(g))


def action_space(graph):
    """

    :param graph: the graph in question
    :return: returns the action space containing valid edges that do not violate the DAG property
    """
    valid_actions_dictionary = {int(node):[] for node, indegree in enumerate(graph.get_in_degrees(graph.get_vertices())) if
                  (indegree > 0 or node < number_input_nodes)}
    to_nodes = [index for index in graph.get_vertices() if index >= number_input_nodes]
    for node, target_list in valid_actions_dictionary.items():
        valid_actions_dictionary[node] = check_acyclic_choice(graph, to_nodes, node)
    #print(valid_actions_dictionary)
    return valid_actions_dictionary


def add_edge(graph):
    from_nodes = [index for index, indegree in enumerate(graph.get_in_degrees(graph.get_vertices())) if
                  (indegree > 0 or index < number_input_nodes)]  # has to either be one of the input nodes OR have information already been sent to it (i.e. indegree>0)
    choice_in = input("choose from " + str(from_nodes) + ": ")
    to_nodes = [index for index in graph.get_vertices() if index >= number_input_nodes]
    valid_to_nodes = check_acyclic_choice(graph, to_nodes, choice_in)
    works = False

    while not works:
        choice_out = input("choose from " + str(valid_to_nodes) + ": ")
        new_edge = graph.add_edge(choice_in, choice_out)
        if not is_DAG(graph):
            print(choice_out + " doesn't work " + str(valid_to_nodes))
            graph.remove_edge(new_edge)
            valid_to_nodes.remove(int(choice_out))
        else:
            works = True


def check_acyclic_choice(graph, possible_nodes, source_node):
    """
    :param possible_nodes: a list of nodes to check as the target node
    :param source_node: a single source node
    :return: a list of nodes that when selected as the target node will not violate the acyclic property of the graph, also removes self referential nodes
    """
    valid_nodes = []
    for node in possible_nodes:
        if not list(all_paths(graph, node, source_node)) and node != source_node:
            valid_nodes.append(node)
        else:
            print(node, " not a valid node")
    return valid_nodes

action_space(g)
print("allpaths", list(all_paths(g, 6, 0)))
if not list(all_paths(g, 6, 0)):
    print("EMPTY")
add_edge(g)
action_space(g)
for path in all_paths(g, 6, 0):
    print("path", path)
print("all paths", list(all_paths(g, 6, 0)))
test = adjacency(g)
print(test.toarray())
print('adj2',adjacency_m.toarray())
add_edge(g)
action_space(g)
test = adjacency(g)
print(test.toarray())
add_edge(g)
action_space(g)
test = adjacency(g)

print(test.toarray())
graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(1000, 1000), output="testenv/test.png")
