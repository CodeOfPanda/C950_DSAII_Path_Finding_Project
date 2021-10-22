# Maggie Leigland Student ID: #001058808

# importing classes
from load_data import load_package_data, load_distance_data, load_all_trucks
from algorithm import NN_shortest_path

pkg_hashmap = load_package_data()  # hash table for package data
graph, vertices = load_distance_data()  # graph data and vertices array
trucks = load_all_trucks(pkg_hashmap)  # trucks 1 - 3 loaded with packages

# Run algorithm for all trucks
total_distance = 0.0

for truck in trucks:
    print(truck.name, " starting route at ", truck.get_leave_time())

    # sets the delivery status to en route once truck leaves
    for pkg in truck.get_packages():
        if pkg.get_id() == 9:
            pkg.set_address("410 S State St")
            pkg.set_city("Salt Lake City")
            pkg.set_zip(84111)
        pkg.set_status("EN ROUTE")
    
    # calls Nearest Neighbor algorithm
    NN_shortest_path(graph, vertices[0], truck, vertices)
    total_distance = total_distance + truck.get_distance()

print("Total distance: ", total_distance)  # total distance traveled by all trucks.
