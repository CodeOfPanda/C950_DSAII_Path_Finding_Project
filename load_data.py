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
    # loading distance data
    with open('./data/WGUPS_Distance_Table.csv', 'r', encoding='utf-8-sig') as dist_data:
        dist_file = dist_data.readlines()
        # taking the header addresses and placing them into an array
        headers = [row.split(',\n') for row in dist_file[:27]]
        # taking only the distance data (miles)
        rows = [row.split(',\n') for row in dist_file[27:]]
        vertices = []
        graph = Graph()

        # creating vertex objects and adding them to an array and the graph
        for line in headers:
            vertex = Vertex(line[0])
            vertices.append(vertex)
            graph.add_vertex(vertex)

        # pairing the correct vertices with the distance between them and adding them to the graph.
        for i, row in enumerate(rows):
            miles = row[0].split(',')
            vertex_1 = vertices[i]

            for j, m in enumerate(miles):
                if m:
                    vertex_2 = vertices[j]
                    # Removing the data for vertex to the same vertex, basically just cleans the data
                    if vertex_1.get_label() != vertex_2.get_label():
                        graph.add_undirected_edge(vertex_1, vertex_2, m)
                else:
                    break

    return graph


# Truck Data
# Create three trucks
t1 = Truck()
t2 = Truck()
t3 = Truck()
# Package ids for each Truck
t1_packages = [6, 25, 26, 31, 32, 28, 34, 39, 35, 33, 27, 24, 23, 22, 17, 12]
t2_packages = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 21, 1, 37, 29, 30, 40]
t3_packages = [5, 9, 2, 4, 7, 8, 10, 11]


def load_all_trucks(hashmap):
    trucks = []
    truck1 = load_truck(t1, t1_packages, hashmap)
    trucks.append(truck1)
    truck2 = load_truck(t2, t2_packages, hashmap)
    trucks.append(truck2)
    truck3 = load_truck(t3, t3_packages, hashmap)
    trucks.append(truck3)
    return trucks


def load_truck(truck, truck_packages, pkg_hashmap):
    for p in truck_packages:
        package = pkg_hashmap.look_up(p)
        truck.load_packages(package)
    return truck
