from models.package import Package
from models.hash_table import HashTable

def load_package_data():
    with open('./data/Package_File.csv', 'r') as package_file:
        file = package_file.readlines()
        data_array = [row.split(',') for row in file]
        data_array.pop(0)  # removing the first element from the array (column headers)
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
            
            pkg = Package(p_id, address, city, state, zip, delivery_deadline, mass_kg, notes, status)
            h.insert(p_id, pkg)
    return h

pkg_hash_map = load_package_data()

print("--------------------------------")
print(pkg_hash_map.print())

        
