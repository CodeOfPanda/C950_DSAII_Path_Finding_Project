class Graph:
    
    # constructor method
    def __init__(self):
        self.adjacency_list = {}
        self.edge_list = {}
        
    # method to add vertex to graph
    def add_vertex(self, new_vertex):
        # creates a dictionary: key - new vertex, value - empty.
        self.adjacency_list[new_vertex] = []
        
    # method that creates a dictionary:
    # key: a tuple with start vertex (location 1) and end vertex (location 2)
    # value: edge's (distance from one location to another)
    def add_edge(self, from_vertex, to_vertex, distance=0.0):
        self.edge_list[(from_vertex, to_vertex)] = distance
        # inserts values into the adjacency list's dictionary.
        self.adjacency_list[from_vertex].append(to_vertex)
        
    # method that calls the above method
    # it calls twice to add an undirected (bidirectional) edge to the graph.
    def add_undirected_edge(self, vertex_1, vertex_2, distance=0.0):
        self.add_edge(vertex_1, vertex_2, distance)
        self.add_edge(vertex_2, vertex_1, distance)
        
    # print method
    def print(self):
        print(self.adjacency_list)
        