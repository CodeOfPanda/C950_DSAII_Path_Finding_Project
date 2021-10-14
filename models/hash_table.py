class HashTable:
    # constructor that sets the table size and each initial element to be empty
    def __init__(self, init_size=40):
        self.init_size = init_size
        self.table = []
        for i in range(init_size):
            self.table.append([])
    
    # the hash function
    # takes the key modulo (tablesize) 
    # gives you the index within the hash table
    def get_hash_index(self, key):
        return hash(key) % self.init_size
    
    # insert function
    # adds new key/value pair into the table.
    def insert(self, key, value):
        key_hash_index = self.get_hash_index(key)  # gets index from hash table
        key_value = [key, value]  # creates array of key/value pair
        
        # checks if the index is empty
        if not self.table[key_hash_index]:
            # adds new pair into index
            self.table[key_hash_index] = list([key_value])
            return True  # breaks 
        else:
            # loops through the list with index for key
            for k_v in self.table[key_hash_index]:
                if k_v[0] == key:  # if found updates value
                    k_v[1] = value
                    return True  # breaks
            # key not found; appends new pair to list.
            self.table[key_hash_index].append(key_value)
            return True  # breaks
    
    # look_up function
    # takes the key and returns the value if found    
    def look_up(self, key):
        key_hash_index = self.get_hash_index(key)  # get index from hash talbe
        
        # checks if index is not empty
        if self.table[key_hash_index]:
            # searches list at index for the key
            for k_v in self.table[key_hash_index]:
                if k_v[0] == key:
                    # returns value if found
                    return k_v[1]
        return None  # returns none if no such key exists.
    
    # remove function
    # deletes a key/value pair from the hash table
    def remove(self, key):
        key_hash_index = self.get_hash_index(key)  # gets index from hash table
        
        # checks to see if the index is empty
        if not self.table[key_hash_index]:
            return False  # if empty return false since no such key exists
        # else loop through list looking for correct key and remove once found.
        for i in range(0, len(self.table[key_hash_index])):
            if self.table[key_hash_index][i][0] == key:  # need to use iterator to have an index value to delete pair
                self.table[key_hash_index].pop(i)
                return True
    
    # prints hash table
    def print(self):
        for k_v in self.table:
            if k_v:
                print(k_v)