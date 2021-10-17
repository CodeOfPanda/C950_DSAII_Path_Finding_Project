from models.truck import Truck
from load_data import load_package_data, load_distance_data

t1 = Truck()
t2 = Truck()
t3 = Truck()
t1_packages = [6, 25, 26, 31, 32, 28, 34, 39, 35, 33, 27, 24, 23, 22, 17, 12]
t2_packages = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 21, 1, 37, 29, 30, 40]
t3_packages = [5, 9, 2, 4, 7, 8, 10, 11]


pkg_hashmap = load_package_data()
graph = load_distance_data()

def load_truck(truck, truck_packages):
    for p in truck_packages:
        package = pkg_hashmap.look_up(p)
        truck.load_packages(package)
        

load_truck(t1, t1_packages)
load_truck(t2, t2_packages)
load_truck(t3, t3_packages)
