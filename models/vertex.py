class Vertex:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.distance = float('inf')
        self.pre_vertex = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
    def get_address(self):
        return self.address
    
    def set_address(self, new_address):
        self.address = new_address
        
    def get_pre_vertex(self):
        return self.pre_vertex
    
    def set_pre_vertex(self, new_pre_vertex):
        self.pre_vertex = new_pre_vertex
    
    def get_distance(self):
        return self.distance
    
    def set_distance(self, new_distance):
        self.distance = new_distance