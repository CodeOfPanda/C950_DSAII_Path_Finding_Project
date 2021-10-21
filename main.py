# Maggie Leigland Student ID: #001058808

# importing classes
from load_data import load_package_data, load_distance_data, load_all_trucks
from models.time import Time

pkg_hashmap = load_package_data()  # hash table for package data
graph, vertices = load_distance_data()  # graph data and vertices array
trucks = load_all_trucks(pkg_hashmap)  # trucks 1 - 3 loaded with packages

# greedy algorithm for delivering packages off of each truck.
def greedy_shortest_path(g, start_vertex, truck):
    # Time object that replaces the time based off truck leave time
    time = Time(hour=truck.get_leave_time().hour, minute=truck.get_leave_time().minute, second=truck.get_leave_time().second) 
    print("In algorithm time: ", time.get_time())
    # Put all vertices in an unvisited queue.
    unvisited_queue = []  # empty array for vertex addresses of delivery locations
    pkg_queue = truck.get_packages()  # array of packages
    
    priority_queue = []  # empty array for packages with a delivery deadline
    
    # looping through the package queue and adding delivery addresses to 
    # the unvisited_queue OR the priority queue ONLY IF the packages are
    # on truck 1.
    for package in pkg_queue:
        for vertex in vertices:
            if package.get_address() == vertex.get_address():
                if truck.name == "Truck 1":
                    if package.get_delivery_deadline() == '10:30 AM':
                        priority_queue.append(vertex)
                unvisited_queue.append(vertex)
    # dedup the data
    queue = set(unvisited_queue)
    unvisited_queue = list(queue)
    
    # Start_vertex has a distance of 0 from itself
    start_vertex.set_distance(0.0)
    #setting current vertext to start vertex for the beginning of the algorithm. current_vertex gets updated throughout
    current_vertex = start_vertex
    truck_distance = float(0.0)
    
    # looping through the unvisited queue and poping (deleting) delivery locations at each stop.
    # Also tracking the distances of each truck as well as the time each package was delivered.
    while len(unvisited_queue) >= 0:
        # this is our base statement that breaks us from the loop. aslo takes the trucks back to the hub.
        if len(unvisited_queue) == 0:
            new_vertex, idx, distance_traveled = calculate_distance([start_vertex], g, current_vertex, pkg_queue, time)
            current_vertex = new_vertex
            time.set_time(truck.calculate_time(distance_traveled))
            print(time.get_time())
            truck_distance = float(truck_distance) + float(distance_traveled)   
            truck.set_distance(truck_distance)
            break
        # calculates the distance traveled by each truck as they deliver packages.
        else: 
            # checks if priority queue is empty before delivering the other packages.
            if len(priority_queue) > 0:
                new_vertex, idx, distance_traveled = calculate_distance(priority_queue, g, current_vertex, pkg_queue, time)
                priority_queue.pop(idx)
                
                # pops off the duplicate package from the unvisited queue.
                for i, p in enumerate(unvisited_queue):
                    if p.get_address() == new_vertex.get_address():
                        unvisited_queue.pop(i)
            # if not truck 1, handles unvisited queue           
            else:
                new_vertex, idx, distance_traveled = calculate_distance(unvisited_queue, g, current_vertex, pkg_queue, time)
                unvisited_queue.pop(idx)
            
        #after loop has ran, update current_vertex
        current_vertex = new_vertex
        #pass in the next distance to be travelled and get seconds passed returned
        time.set_time(truck.calculate_time(distance_traveled))
        print(time.get_time())
        truck_distance = float(truck_distance) + float(distance_traveled) # updates truck distance  
        truck.set_distance(truck_distance)
        
    print("Truck distance was: ", truck.get_distance())

# called within the greedy algorithm function
# calculates the distances between delivery locations and chooses the closer location.
# returns new vertex, the index for the unvisited/priority queue to pop vertex.
def calculate_distance(queue, g, current_vertex, pkg_queue, time):
    shortest_distance = float('inf')
    for i, delivery_loc in enumerate(queue):
            # loop through each tuple pair in edge list { (from_vertex, to_vertex) : miles }
            for k,v in g.edge_list.items():
                # if from vertex in tuple matches current_vertex address
                if k[0].get_address() == current_vertex.get_address():
                    # if to vertex in tuple matches delivery location address
                    if k[1].get_address() == delivery_loc.get_address():                   
                        # if distance to new vertex is closest, update values
                        if float(g.edge_list[k]) < float(shortest_distance):
                            shortest_distance = g.edge_list[k] # miles
                            new_vertex = k[1]
                            idx = i
    
    print('From ',current_vertex.get_name(), ' to ',new_vertex.get_name(),' is ',shortest_distance, ' miles')
    # loop through the packages on the truck and set their status as delivered and sets their time of delivery once at location
    for pkg in pkg_queue:
        if pkg.get_address() == new_vertex.get_address():
            pkg.set_status("DELIVERED") 
            pkg.set_delivery_time(time.get_time())
            print("Deadline: ",pkg.get_delivery_deadline())
            print("Delivered at: ",pkg.get_delivery_time())

    return new_vertex, idx, shortest_distance

# Run algorithm for all trucks
total_distance = 0.0

for truck in trucks:
    print(truck.name, " starting route at ", truck.get_leave_time())

    # sets the delivery status to en route once truck leaves
    for pkg in truck.get_packages():
        pkg.set_status("EN ROUTE")
    
    # calls greedy algorithm
    greedy_shortest_path(graph, vertices[0], truck)
    total_distance = total_distance + truck.get_distance()

print("Total distance: ", total_distance)  # total distance traveled by all trucks.
