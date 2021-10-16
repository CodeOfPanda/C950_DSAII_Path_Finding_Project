from models.package import Package
from models.hash_table import HashTable
from models.vertex import Vertex
from models.graph import Graph


def load_package_data():
    with open('./data/Package_File.csv', 'r') as package_file:
        file = package_file.readlines()
        data_array = [row.split(',') for row in file]
        # removing the first element from the array (column headers)
        data_array.pop(0)
        h = HashTable()

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
            h.insert(p_id, pkg)
    return h

# pkg_hash_map = load_package_data()

# print("--------------------------------")
# print(pkg_hash_map.print())


def load_distance_data():
    # loading header data to created vertices
    with open('./data/WGUPS_Distance_Table.csv', 'r', encoding='utf-8-sig') as dist_header_data:
        header_file = dist_header_data.readlines()
        headers = [row.split(',\n') for row in header_file[:27]]
        vertices = []
        graph = Graph()

        for line in headers:
            vertex = Vertex(line[0])
            vertices.append(vertex)
            graph.add_vertex(vertex)

    with open('./data/WGUPS_Distance_Table.csv', 'r', encoding='utf-8-sig') as dist_row_data:
        row_file = dist_row_data.readlines()
        rows = [line.split(',\n') for line in row_file[27:]]

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

    return vertices


distance_rows = load_distance_data()
