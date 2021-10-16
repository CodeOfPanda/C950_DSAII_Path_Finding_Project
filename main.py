from models.package import Package
from models.hash_table import HashTable
from models.vertex import Vertex
from models.graph import Graph


def load_package_data():
    # loading package data 
    with open('./data/Package_File.csv', 'r') as package_file:
        file = package_file.readlines()
        data_array = [row.split(',') for row in file]
        data_array.pop(0)  # removing the first element from the array (column headers)
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
            
            pkg = Package(p_id, address, city, state, zip, delivery_deadline, mass_kg, notes, status)
            h.insert(p_id, pkg)  # inserting the key/value pair into the hash_table
    return h

# pkg_hash_map = load_package_data()

# print("--------------------------------")
# print(pkg_hash_map.print())

def load_distance_data():
    # loading header data
    with open('./data/WGUPS_Distance_Table.csv', 'r', encoding='utf-8-sig') as dist_header_data:
        header_file = dist_header_data.readlines()
        headers = [row.split(',\n') for row in header_file[:27]]  # taking the header addresses and placing them into an array
        vertices = [] 
        graph = Graph()
        
        # creating vertex objects and adding them to an array and the graph
        for line in headers:
            vertex = Vertex(line[0])
            vertices.append(vertex)
            graph.add_vertex(vertex)
            
    # loading row data      
    with open('./data/WGUPS_Distance_Table.csv', 'r', encoding='utf-8-sig') as dist_row_data:
        row_file = dist_row_data.readlines()
        rows = [line.split(',\n') for line in row_file[27:]]  # taking only the distance data (miles)
        
        # pairing the correct vertices with the distance between them and adding them to the graph.
        for i, row in enumerate(rows):
            miles = row[0].split(',')
            vertex_1 = vertices[i]
            for j, m in enumerate(miles):
                if not m:
                    break
                vertex_2 = vertices[j]
                graph.add_undirected_edge(vertex_1, vertex_2, m)
                  
        for k,v in graph.adjacency_list.items():
            print(k.get_label())
            print("--")
            for vertex in v:
                print(vertex.get_label())
            print("-----------")
            
    return vertices


distance_rows = load_distance_data()
