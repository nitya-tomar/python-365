# Problem 4: SRE-flavored — check "server status" from a dict
server = {"name": "web-01", "cpu_usage": 85}
if server["cpu_usage"] == 80:
    print(server["name"], "is under high load")
else:
    print(server["name"], "is healthy")    

server = {"name": "web-01", "cpu_usage": 85, "region": "us-east-1"}

for key, value in server.items():
    print(key, ":", value)