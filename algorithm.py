from models.time import Time

# Nearest Neighbor algorithm for delivering packages off of each truck.
# Big O(N^2)
def NN_shortest_path(g, start_vertex, truck, vertices):
    # Time object that replaces the time based off truck leave time
    time = Time(hour=truck.get_leave_time().hour, minute=truck.get_leave_time().minute, second=truck.get_leave_time().second) 

    # Put all vertices in an unvisited queue.
    unvisited_queue = []  # empty array for vertex addresses of delivery locations
    pkg_queue = truck.get_packages()  # array of packages
    
    priority_queue = []  # empty array for packages with a delivery deadline
    
    # looping through the package queue and adding delivery addresses to 
    # the unvisited_queue OR the priority queue ONLY IF the packages are
    # on truck 1.
    # Big O(N^2) since we are working fixed size arrays
    for package in pkg_queue:  # O(N) because pkg_queue is always going to be and array of 16 elements
        for vertex in vertices:  # O(N), if I had to add vertices dynamically it would be O(N)
            if package.get_address() == vertex.get_address():
                if truck.name == "Truck 1":
                    if package.get_delivery_deadline() == '10:30 AM':
                        priority_queue.append(vertex)
                unvisited_queue.append(vertex)
    # dedup the data
    queue = set(unvisited_queue)
    unvisited_queue = list(queue)
    
    #setting current vertext to start vertex for the beginning of the algorithm. current_vertex gets updated throughout
    current_vertex = start_vertex
    truck_distance = float(0.0)
    
    # looping through the unvisited queue and poping (deleting) delivery locations at each stop.
    # Also tracking the distances of each truck as well as the time each package was delivered.
    # Big O(N^2)
    while len(unvisited_queue) >= 0:
        # this is our base statement that breaks us from the loop. aslo takes the trucks back to the hub.
        if len(unvisited_queue) == 0:
            new_vertex, idx, distance_traveled = calculate_distance([start_vertex], g, current_vertex, pkg_queue, time)  # this function has O(N^2)
            current_vertex = new_vertex
            time.set_time(truck.calculate_time(distance_traveled))
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
                for i, p in enumerate(unvisited_queue):  # O(N)
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
        truck_distance = float(truck_distance) + float(distance_traveled) # updates truck distance  
        truck.set_distance(truck_distance)
        
    truck.set_end_time(time.get_time())

# called within the Nearest Neighbor algorithm function
# calculates the distances between delivery locations and chooses the closer location.
# returns new vertex, the index for the unvisited/priority queue to pop vertex.
# Big O(N^2)
def calculate_distance(queue, g, current_vertex, pkg_queue, time):
    shortest_distance = float('inf')
    for i, delivery_loc in enumerate(queue):  # O(N)
            # loop through each tuple pair in edge list { (from_vertex, to_vertex) : miles }
            for k,v in g.edge_list.items():  # O(N)
                # if from vertex in tuple matches current_vertex address
                if k[0].get_address() == current_vertex.get_address():
                    # if to vertex in tuple matches delivery location address
                    if k[1].get_address() == delivery_loc.get_address():                   
                        # if distance to new vertex is closest, update values
                        if float(g.edge_list[k]) < float(shortest_distance):
                            shortest_distance = g.edge_list[k] # miles
                            new_vertex = k[1]
                            idx = i
    
    # loop through the packages on the truck and set their status as delivered and sets their time of delivery once at location
    for pkg in pkg_queue:
        if pkg.get_address() == new_vertex.get_address():
            pkg.set_status("DELIVERED") 
            pkg.set_delivery_time(time.get_time())

    return new_vertex, idx, shortest_distance
