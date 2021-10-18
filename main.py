# Maggie Leigland Student ID: #001058808

from load_data import load_package_data, load_distance_data, load_all_trucks

pkg_hashmap = load_package_data()
graph, vertices = load_distance_data()
trucks = load_all_trucks(pkg_hashmap)


def dijkstra_shortest_path(g, start_vertex, pkg_queue):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    
    for package in pkg_queue:
        for vertex in vertices:
            if package.get_address() == vertex.get_address():
                unvisited_queue.append(vertex)
    #dedup the data 
    queue = set(unvisited_queue)
    unvisited_queue = list(queue)

    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            #print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pre_vertex)
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        print("From Start Vetex to current_vertex.label: " + current_vertex.label +" distance: " + str(current_vertex.distance))

        #Check potential path lengths from the current vertex to all neighbors. values from  dictionary
        for adj_vertex in g.adjacency_list[current_vertex]:
            # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3], if vertex_2 => adj_vertex in [vertex_6], ...
            # values from dictionary
            edge_weight = g.edge_list[(current_vertex, adj_vertex)]
            # edge_weight = 484 then 626 then 1306, ...}
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pre_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pre_vertex
    path = start_vertex.label + path
    return path

# Run Dijkstra algorithm for all trucks
for truck in trucks:
    dijkstra_shortest_path(graph, vertices[0], truck.get_packages())

# print("\nDijkstra shortest path:")
# for v in graph.adjacency_list:
#     if v.pre_vertex is None and v is not start_vertex:
#         print("1 to %s ==> no path exists" % v.label)
#     else:
#         print("1 to %s ==> %s (total distance: %g)" %
#               (v.label, get_shortest_path(start_vertex, v), v.distance))
