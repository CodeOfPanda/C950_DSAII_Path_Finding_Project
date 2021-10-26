# Maggie Leigland Student ID: #001058808

# importing classes
from load_data import load_package_data, load_distance_data, load_all_trucks  # functions for loading data
from algorithm import NN_shortest_path 
from helpers.print_UI import print_all_pkgs, print_one_pkg, print_truck_data  # functions for user interface
from helpers.calculate_PM_time import get_PM_time
import datetime

pkg_hashmap, all_pkgs = load_package_data()  # hash table for package data and array of all packages
graph, vertices = load_distance_data()  # graph data and vertices array
trucks = load_all_trucks(pkg_hashmap)  # trucks 1 - 3 loaded with packages

# Run algorithm for all trucks
total_distance = 0.0

for truck in trucks:
    # print(truck.name, " starting route at ", truck.get_leave_time())
    # sets the delivery status to en route once truck leaves
    for pkg in truck.get_packages():
        # updating package 9's address
        if pkg.get_id() == 9:
            pkg.set_address("410 S State St")
            pkg.set_city("Salt Lake City")
            pkg.set_zip(84111)
        pkg.set_status("EN ROUTE")  # updating package status after leaving hub
        pkg.set_start_time(truck.get_leave_time())  # capturing trucks start time 
        pkg.set_truck(truck.name)
    
    # calls Nearest Neighbor algorithm
    NN_shortest_path(graph, vertices[0], truck, vertices)
    total_distance = total_distance + truck.get_distance()  # updates total mileage

# prints trucks start/finish time & total mileage for all trucks
print_truck_data(trucks, total_distance)



# loop for user interface
user_input = 0
while(user_input != 5):
    
    print("Select from the following:")
    print("1 = Print ALL packages and corresponding information.")
    print("2 = Enter package ID and a time to view package information.")
    print("3 = Print truck start/finish time and total mileage.")
    print("4 = Print screenshots.")
    print("5 = Exit program.")

    _input = input()
    
    while (_input not in ['1','2','3','4','5']):
        print("Sorry, invalid Entry")
        _input = input("Please enter a valid number 1-5: ")
        
    user_input = int(_input)    
    print('----------------------------------------------------------------')

    # calls functions to print All pkg data and truck data
    if user_input == 1:
        user_time = input("Enter a time (hour:minute): ")
        time_of_day = input("AM or PM? ")   
        while True:
            if time_of_day in ['PM', 'pm']:
                input_time = get_PM_time(user_time)
                print_all_pkgs(all_pkgs, input_time)
                print_truck_data(trucks, total_distance)
                break
            elif time_of_day in ['AM', 'am']:
                input_time = datetime.datetime.strptime(user_time, '%H:%M').time()
                print_all_pkgs(all_pkgs, input_time)
                print_truck_data(trucks, total_distance)
                break    
            else: 
                print("Sorry, invalid Entry")
                user_time = int(input("Enter AM or PM: "))   
        
    # calls functions to print single pkg data and truck data
    elif user_input == 2:
        user_id = int(input("Enter Package ID: "))
        while True:     
            # boundry test for user id
            if user_id > 0 and user_id < 41:
                user_time = input("Enter a time (hour:minute): ")
                time_of_day = input("AM or PM? ")
                if time_of_day in ['PM', 'pm']:
                    input_time = get_PM_time(user_time)
                    print_one_pkg(all_pkgs, input_time, user_id)
                    print_truck_data(trucks, total_distance)
                    break
                elif time_of_day in ['AM', 'am']:
                    input_time = datetime.datetime.strptime(user_time, '%H:%M').time()
                    print_one_pkg(all_pkgs, input_time, user_id)
                    print_truck_data(trucks, total_distance)
                    break       
                else: 
                    print("Sorry, invalid Entry")
                    user_time = int(input("Enter AM or PM: "))    
            else: 
                print("Sorry, invalid ID")
                user_id = int(input("Enter Package ID: "))
        
    # calls function to print truck data                    
    elif user_input == 3:
        print_truck_data(trucks, total_distance)
    elif user_input == 4:
        print("8:35 a.m.")
        input_time = datetime.datetime.strptime("8:35", '%H:%M').time()
        print_all_pkgs(all_pkgs, input_time)
        print_truck_data(trucks, total_distance)
        print("9:40 a.m.")
        input_time = datetime.datetime.strptime("9:40", '%H:%M').time()
        print_all_pkgs(all_pkgs, input_time)
        print_truck_data(trucks, total_distance)
        print("1:00 p.m.")
        input_time = get_PM_time("1:00")
        print_all_pkgs(all_pkgs, input_time)
        print_truck_data(trucks, total_distance)
    # break statement   
    elif user_input == 5:
        break;
    # invalid entry
    else:
        print("Sorry, not a valid input. Try again\n")
        
