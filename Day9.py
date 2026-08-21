# Q3 — Build a list from a dictionary
unhealthy_servers = []
servers = {"web-01": 92, "web-02": 45, "web-03": 88}

for name, usage in servers.items():
    if usage > 80:
        unhealthy_servers.append(name)

print(unhealthy_servers)
