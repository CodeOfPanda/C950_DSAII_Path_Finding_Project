# Maggie Leigland Student ID: #001058808

from load_data import load_package_data, load_distance_data, load_all_trucks
import datetime

pkg_hashmap = load_package_data()
graph, vertices = load_distance_data()
trucks = load_all_trucks(pkg_hashmap)
today = datetime.datetime.now()
time = today.replace(hour=8, minute=00, second=0, microsecond=0)
print("Starting time: ", time.time())

def greedy_shortest_path(g, start_vertex, truck, time):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    pkg_queue = truck.get_packages()
    
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
    truck_distance = float(0.0)
    
    while len(unvisited_queue) >= 0:
        if len(unvisited_queue) == 0:
            new_vertex, idx, shortest_distance = calculate_distance([start_vertex], g, current_vertex, pkg_queue)
            break
        else:
            new_vertex, idx, shortest_distance = calculate_distance(unvisited_queue, g, current_vertex, pkg_queue)
            
        #after loop has ran, update current_vertex
        current_vertex = new_vertex
        unvisited_queue.pop(idx)
        #pass in the next distance to be travelled and get seconds passed returned
        time = time + datetime.timedelta(seconds=truck.calculate_time(shortest_distance))
        print("Time: ", time.time())
        truck_distance = float(truck_distance) + float(shortest_distance)
                   
    truck.set_distance(truck_distance)
    print("Truck distance was: ", truck_distance)

def calculate_distance(queue, g, current_vertex, pkg_queue):
    shortest_distance = float('inf')
    for i, delivery_loc in enumerate(queue):
            #loop through each tuple pair in edge list
            for k,v in g.edge_list.items():
                #if from vertex in tuple matches current_vertex address
                if k[0].get_address() == current_vertex.get_address():
                    #if to vertex in tuple matches delivery location address
                    if k[1].get_address() == delivery_loc.get_address():                   
                        #if distance to new vertex is closest, update values
                        if float(g.edge_list[k]) < float(shortest_distance):
                            shortest_distance = g.edge_list[k] #miles
                            new_vertex = k[1]
                            idx = i
    
    print('From ',current_vertex.get_name(), ' to ',new_vertex.get_name(),' is ',shortest_distance, ' miles')
    #loop through the packages on the truck and set their status as delivered if at location
    for pkg in pkg_queue:
        if pkg.get_address() == new_vertex.get_address():
            pkg.set_status("DELIVERED")    

    return new_vertex, idx, shortest_distance

# Run algorithm for all trucks
total_distance = 0.0
num = 1
for truck in trucks:
    print("Path for truck: ", num)
    #set the status for packages on truck as 'en route'
    for pkg in truck.get_packages():
        pkg.set_status("EN ROUTE")
    greedy_shortest_path(graph, vertices[0], truck, time)
    num+=1
    total_distance = total_distance + truck.get_distance()

print("Total distance: ", total_distance)