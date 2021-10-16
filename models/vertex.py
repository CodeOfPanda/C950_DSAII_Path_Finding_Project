class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pre_vertex = None
    
    def get_label(self):
        return self.label
    
    def set_label(self, label):
        self.label = label