class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pre_vertex = None
    
    