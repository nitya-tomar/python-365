def is_zombie(days_unused):
    if days_unused > 90:
        return True
    else:
        return False

keys = {"key1": 45, "key2": 120, "key3": 200}

for k, v in keys.items():
    if is_zombie(v):
        print(k, "- ZOMBIE KEY")
    else:
        print(k, "- active")

# Write a function called check_cpu that takes a server name and its usage, and returns "ALERT" if usage is above 80, or "OK" otherwise.
def check_cpu(server_name, usage):
    if usage > 80:
        return "ALERT"
    else:
        return "OK"

servers = {"web-01": 92, "web-02": 45, "web-03": 88}

for name, usage in servers.items():
    status = check_cpu(name, usage)
    print(name, "-", status)