from models.package import Package
from models.hash_table import HashTable
from models.vertex import Vertex
from models.graph import Graph
from models.truck import Truck


def load_package_data():
    # loading package data
    with open('./data/Package_File.csv', 'r') as package_file:
        file = package_file.readlines()
        data_array = [row.split(',') for row in file]
        # removing the first element from the array (column headers)
        data_array.pop(0)
        h = HashTable()

        # creating a new package object from each row of data in the data_array
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

            pkg = Package(p_id, address, city, state, zip,
                          delivery_deadline, mass_kg, notes, status)
            # inserting the key/value pair into the hash_table
            h.insert(p_id, pkg)
    return h


def load_distance_data():
    vertices = []
    graph = Graph()

    #load delivery locations and addresses
    with open('./data/Delivery_Locations.csv', 'r') as location_data:
        loc_file = location_data.readlines()
        headers = [row.split(',\n') for row in loc_file]
        header_data = [loc[0].split(', ') for loc in headers]
        
        for data in header_data:
            name = data[0]
            address = data[1]
            # creating vertex objects and adding them to an array and the graph
            vertex = Vertex(name=name, address=address)
            vertices.append(vertex)
            graph.add_vertex(vertex)
                
    # loading distance data
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
def load_all_trucks(hashmap):
    # Create three trucks
    t1 = Truck()
    t2 = Truck()
    t3 = Truck()
    # Package ids for each Truck
    t1_packages = [6, 25, 26, 31, 32, 28, 34, 39, 35, 33, 27, 24, 23, 22, 17, 12]
    t2_packages = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 21, 1, 37, 29, 30, 40]
    t3_packages = [5, 9, 2, 4, 7, 8, 10, 11]
    trucks = []
    truck1 = load_truck(t1, t1_packages, hashmap)
    trucks.append(truck1)
    truck2 = load_truck(t2, t2_packages, hashmap)
    trucks.append(truck2)
    truck3 = load_truck(t3, t3_packages, hashmap)
    trucks.append(truck3)
    return trucks

# loading each truck with their package objects.
def load_truck(truck, truck_packages, pkg_hashmap):
    for p in truck_packages:
        package = pkg_hashmap.look_up(p)
        truck.load_packages(package)
    return truck
