class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_list = {}
        
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        
    def add_edge(self, from_vertex, to_vertex, distance=0.0):
        self.edge_list[(from_vertex, to_vertex)] = distance
        self.adjacency_list[from_vertex].append(to_vertex)
        
    def add_undirected_edge(self, vertex_1, vertex_2, distance=0.0):
        self.add_edge(vertex_1, vertex_2, distance)
        self.add_edge(vertex_2, vertex_1, distance)
        
    def print(self):
        print(self.adjacency_list)
        