class Vertex:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
    def get_address(self):
        return self.address
    
    def set_address(self, new_address):
        self.address = new_address