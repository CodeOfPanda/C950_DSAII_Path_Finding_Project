from load_data import load_package_data, load_distance_data, load_all_trucks

pkg_hashmap = load_package_data()
graph = load_distance_data()
t1, t2, t3 = load_all_trucks(pkg_hashmap)
