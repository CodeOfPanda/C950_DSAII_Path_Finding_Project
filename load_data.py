from models.package import Package
from models.hash_table import HashTable
from models.vertex import Vertex
from models.graph import Graph
from models.truck import Truck

# function that is responsible for loading the package data from the package_file.csv file
# creates a package object for each line of the file and inserts it into the hash table 
# returns the hash table
# Big O(N)
def load_package_data():
    # loading package data
    with open('./data/WGUPS_Package_File.csv', 'r') as package_file:
        file = package_file.readlines()
        # spliting the data into individual array elements
        data_array = [row.split(',') for row in file]
        # removing the first element from the array (column headers)
        data_array.pop(0)
        h = HashTable()
        all_pkgs = []

        # assigning data to the corect variable to be passed into the Package constructor 
        for data in data_array:
            p_id = int(data[0])
            address = data[1]
            city = data[2]
            state = data[3]
            zip = int(data[4])
            delivery_deadline = data[5]            
            mass_kg = int(data[6])
            notes = data[7]
            status = 'AT_HUB'

            # creating a new package object from each row of data in the data_array
            pkg = Package(p_id, address, city, state, zip,
                          delivery_deadline, mass_kg, notes, status)
            # inserting the key/value pair into the hash_table
            h.insert(p_id, pkg)
            all_pkgs.append(pkg)
    return h, all_pkgs

# function responsible for loading the distance data and delivery location data in from their csv files.
# creates a graph based off vertex names and locations
# returns both the graph and the array containing vertex objects 
# Big O(N^2)
def load_distance_data():
    vertices = []
    graph = Graph()

    #load delivery locations and addresses
    # Big O(N)
    with open('./data/Delivery_Locations.csv', 'r') as location_data:
        loc_file = location_data.readlines()
        # splits each line of data into array elements
        headers = [row.split(',\n') for row in loc_file]
        # splits each string into seperate elements with in the above array. 
        header_data = [loc[0].split(', ') for loc in headers]
        
        for data in header_data:
            name = data[0]
            address = data[1]
            # creating vertex objects and adding them to an array and the graph
            vertex = Vertex(name=name, address=address)
            vertices.append(vertex)
            graph.add_vertex(vertex)
                
    # loading distance data
    # Big O(N^2)
    with open('./data/WGUPS_Distance_Table.csv', 'r', encoding='utf-8-sig') as dist_data:
        dist_file = dist_data.readlines()
        # taking only the distance data (miles)
        rows = [row.split(',\n') for row in dist_file[27:]]
        
        # pairing the correct vertices with the distance between them and adding them to the graph.
        for i, row in enumerate(rows):
            miles = row[0].split(',')
            vertex_1 = vertices[i]

            for j, m in enumerate(miles):
                if m:
                    vertex_2 = vertices[j]
                    # Removing the data for vertex to the same vertex, basically just cleans the data
                    if vertex_1.get_name() != vertex_2.get_name():
                        graph.add_undirected_edge(vertex_1, vertex_2, m)
                else:
                    break

    return [graph, vertices]


# creating an array of trucks with their unique packages.
# Big O(N) since it calls the function load_truck that has an O(N) runtime.
def load_all_trucks(hashmap):
    # Create three truck objects
    t1 = Truck(9,5,0, 'Truck 1')
    t2 = Truck(8,0,0, 'Truck 2')
    t3 = Truck(10,27,0, 'Truck 3')

    # Package id's for each Truck
    t1_packages = [6, 25, 26, 31, 32, 28, 34, 39, 35, 33, 27, 24, 23, 22, 17, 12]
    t2_packages = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 21, 1, 37, 29, 30, 40]
    t3_packages = [5, 9, 2, 4, 7, 8, 10, 11]
    # array for truck data that is returned from the function load_truck.
    trucks = []
    truck1 = load_truck(t1, t1_packages, hashmap)
    trucks.append(truck1)
    truck2 = load_truck(t2, t2_packages, hashmap)
    trucks.append(truck2)
    truck3 = load_truck(t3, t3_packages, hashmap)
    trucks.append(truck3)
    return trucks

# loading each truck with their package objects.
# Big O(N)
def load_truck(truck, truck_packages, pkg_hashmap):
    for p in truck_packages:
        package = pkg_hashmap.look_up(p)
        truck.load_packages(package)
    return truck
