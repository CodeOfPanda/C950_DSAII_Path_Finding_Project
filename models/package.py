class Package:
    # constructor
    def __init__(self, p_id, address, city, state, _zip, delivery_deadline, mass_kg, notes, status='At_HUB'):
        self.p_id = p_id
        self.address = address
        self.city = city
        self.state = state
        self._zip = _zip
        self.delivery_deadline = delivery_deadline
        self.mass_kg = mass_kg
        self.notes = notes
        self.status = status
        self.delivery_time = None
        self.start_time = None
      
    # getters 
    def get_id(self):
        return self.p_id
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip(self):
        return self._zip
    
    def get_delivery_deadline(self):
        return self.delivery_deadline
    
    def get_mass_kg(self):
        return self.mass_kg
    
    def get_notes(self):
        return self.notes
    
    def get_status(self):
        return self.status
    
    def get_delivery_time(self):
        return self.delivery_time
    
    def get_start_time(self):
        return self.start_time
    
    # setters 
    def set_id(self, p_id):
        self.p_id = p_id
        
    def set_address(self, address):
        self.address = address
        
    def set_city(self, city):
        self.city = city
        
    def set_state(self, state):
        self.state = state
    
    def set_zip(self, _zip):
        self._zip = _zip
    
    def set_delivery_deadline(self, delivery_deadline):
        self.delivery_deadline = delivery_deadline
    
    def set_weight(self, weight):
        self.mass_kg = weight
        
    def set_notes(self, notes):
        self.notes = notes
        
    def set_status(self, status):
        self.status = status
        
    def set_delivery_time(self, new_time):
        self.delivery_time = new_time
        
    def set_start_time(self, new_time):
        self.start_time = new_time
        
    def print_pkg(self, ID):
        print(self.get_ID(ID), "\t", self.get_address(), "\t", )