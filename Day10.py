def is_zombie(days_unused):
    return days_unused > 90

def zombie_report(keys_dict):
    # loop through keys_dict
    for key, days_unused in keys_dict.items():
        # use is_zombie() inside this function to check each value
        if is_zombie(days_unused):
            print(key, ": ZOMBIE")
        else:
            print(key, ": active")
