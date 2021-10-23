# Maggie Leigland Student ID: #001058808

# importing classes
from load_data import load_package_data, load_distance_data, load_all_trucks
from algorithm import NN_shortest_path
from helpers.print_UI import print_all_pkgs, print_one_pkg, print_truck_data


pkg_hashmap, all_pkgs = load_package_data()  # hash table for package data and array of all packages
graph, vertices = load_distance_data()  # graph data and vertices array
trucks = load_all_trucks(pkg_hashmap)  # trucks 1 - 3 loaded with packages

# Run algorithm for all trucks
total_distance = 0.0

for truck in trucks:
    # print(truck.name, " starting route at ", truck.get_leave_time())
    # sets the delivery status to en route once truck leaves
    for pkg in truck.get_packages():
        if pkg.get_id() == 9:
            pkg.set_address("410 S State St")
            pkg.set_city("Salt Lake City")
            pkg.set_zip(84111)
        pkg.set_status("EN ROUTE")
        pkg.set_start_time(truck.get_leave_time())
        # print("Package start time is: ", pkg.get_start_time())
    
    # calls Nearest Neighbor algorithm
    NN_shortest_path(graph, vertices[0], truck, vertices)
    total_distance = total_distance + truck.get_distance()

print_truck_data(trucks, total_distance)

user_input = 0
while(user_input != 4):
    
    print("Select from the following:")
    print("1 = Print ALL packages and corresponding information.")
    print("2 = Enter package ID and a time to view package information.")
    print("3 = Print truck start/finish time and total mileage.")
    print("4 = Exit program.")

    user_input = int(input())
    print('----------------------------------------------------------------')

    if user_input == 1:
        user_time = input("Enter a time (hour:minute): ")        
        print_all_pkgs(all_pkgs, user_time)
        print_truck_data(trucks, total_distance)

    elif user_input == 2:
        user_id = int(input("Enter Package ID: "))
        user_time = input("Enter a time (hour:minute): ")
        
        # boundry test for user id
        if user_id > -1 and user_id < 41:
            print_one_pkg(all_pkgs, user_time, user_id)
        else: 
            print("Sorry, invalid ID")
            user_id = int(input("Enter Package ID: "))
        
        print_truck_data(trucks, total_distance)
                    
    elif user_input == 3:
        print_truck_data(trucks, total_distance)        
        
    elif user_input == 4:
        break;
    else:
        print("Sorry, not a valid input. Try again\n")
        
