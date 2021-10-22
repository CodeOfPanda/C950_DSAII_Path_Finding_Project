import datetime

def print_all_pkgs(all_pkgs, user_time):
    input_time = datetime.datetime.strptime(user_time, '%H:%M').time()
    
    for pkg in all_pkgs:
        if input_time < pkg.get_start_time():
            print("Package ID: ", pkg.get_id(), "\tAddress: ", pkg.get_address(), "\tDelivery Deadline: ", pkg.get_delivery_deadline(), "\t City: ", pkg.get_city(), "\t zip code:", pkg.get_zip(),
            "\t Weight: ", pkg.get_mass_kg(), "kg", "\tDelivery Status: At the Hub")
            
        elif input_time > pkg.get_start_time() and input_time < pkg.get_delivery_time():
            print("Package ID: ", pkg.get_id(), "\tAddress: ", pkg.get_address(), "\tDelivery Deadline: ", pkg.get_delivery_deadline(), "\t City: ", pkg.get_city(), "\t zip code:", pkg.get_zip(),
            "\t Weight: ", pkg.get_mass_kg(), "kg", "\tDelivery Status: En Route")
            
        elif input_time > pkg.get_start_time() and input_time > pkg.get_delivery_time():
            print("Package ID: ", pkg.get_id(), "\tAddress: ", pkg.get_address(), "\tDelivery Deadline: ", pkg.get_delivery_deadline(), "\t City: ", pkg.get_city(), "\t zip code:", pkg.get_zip(),
            "\t Weight: ", pkg.get_mass_kg(), "kg", "\tDelivery Status: Delivered", "\tDelivered at ", pkg.get_delivery_time())
    print()

def print_one_pkg(all_pkgs, user_time, user_id):
    input_time = datetime.datetime.strptime(user_time, '%H:%M').time()
    
    for pkg in all_pkgs:
            if pkg.get_id() == user_id:
                if input_time < pkg.get_start_time():
                    print("Package ID: ", pkg.get_id(), "\tAddress: ", pkg.get_address(), "\tDelivery Deadline: ", pkg.get_delivery_deadline(), "\t City: ", pkg.get_city(), "\t zip code:", pkg.get_zip(),
                    "\t Weight: ", pkg.get_mass_kg(), "kg", "\tDelivery Status: At the Hub")
                
                elif input_time > pkg.get_start_time() and input_time < pkg.get_delivery_time():
                    print("Package ID: ", pkg.get_id(), "\tAddress: ", pkg.get_address(), "\tDelivery Deadline: ", pkg.get_delivery_deadline(), "\t City: ", pkg.get_city(), "\t zip code:", pkg.get_zip(),
                    "\t Weight: ", pkg.get_mass_kg(), "kg", "\tDelivery Status: En Route")
                    
                elif input_time > pkg.get_start_time() and input_time > pkg.get_delivery_time():
                    print("Package ID: ", pkg.get_id(), "\tAddress: ", pkg.get_address(), "\tDelivery Deadline: ", pkg.get_delivery_deadline(), "\t City: ", pkg.get_city(), "\t zip code:", pkg.get_zip(),
                    "\t Weight: ", pkg.get_mass_kg(), "kg", "\tDelivery Status: Delivered", "\tDelivered at ", pkg.get_delivery_time())
    print()