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
    # dedup the data 
    queue = set(unvisited_queue)
    unvisited_queue = list(queue)

    # Start_vertex has a distance of 0 from itself
    start_vertex.set_distance(0.0)
    #setting current vertext to start vertex for the beginning of the algorithm. current_vertex gets updated throughout
    current_vertex = start_vertex
    total_distance = float(0.0)
    
    while len(unvisited_queue) >= 0:
        if len(unvisited_queue) == 0:
            new_vertex, idx, shortest_distance = calculate_distance([start_vertex], g, current_vertex)
            break
        else:
            new_vertex, idx, shortest_distance = calculate_distance(unvisited_queue, g, current_vertex)
        
        #after loop has ran, update current_vertex
        current_vertex = new_vertex
        print("Current vertex is now: ", current_vertex.get_name())
        print("Removing ", unvisited_queue[idx].get_name(), "....")
        unvisited_queue.pop(idx)
        total_distance = float(total_distance) + float(shortest_distance)
                   
    print("Total distance was: ", total_distance)

def calculate_distance(queue, g, current_vertex):
    shortest_distance = float('inf')
    for i, delivery_loc in enumerate(queue):
            #loop through each tuple pair in edge list
            for k,v in g.edge_list.items():
                #if from vertex in tuple matches current_vertex address
                if k[0].get_address() == current_vertex.get_address():
                    #if to vertex in tuple matches delivery location address
                    if k[1].get_address() == delivery_loc.get_address():
                        print('From ',k[0].get_name(), ' to ',k[1].get_name(),' is ',g.edge_list[k], ' miles')
                        
                        #if distance to new vertex is closest, update values
                        if float(g.edge_list[k]) < float(shortest_distance):
                            shortest_distance = g.edge_list[k] #miles
                            new_vertex = k[1]
                            idx = i
    return new_vertex, idx, shortest_distance

def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pre_vertex
    path = start_vertex.label + path
    return path

# t1 = [trucks[0]]
# Run Dijkstra algorithm for all trucks
num = 1
for truck in trucks:
    print("Path for truck: ", num)
    dijkstra_shortest_path(graph, vertices[0], truck.get_packages())
    num+=1

# print("\nDijkstra shortest path:")
# for v in graph.adjacency_list:
#     if v.pre_vertex is None and v is not start_vertex:
#         print("1 to %s ==> no path exists" % v.label)
#     else:
#         print("1 to %s ==> %s (total distance: %g)" %
#               (v.label, get_shortest_path(start_vertex, v), v.distance))
