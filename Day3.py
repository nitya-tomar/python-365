# Problem 4: SRE-flavored — check "server status" from a dict
server = {"name": "web-01", "cpu_usage": 85}
if server["cpu_usage"] == 80:
    print(server["name"], "is under high load")
else:
    print(server["name"], "is healthy")    

server = {"name": "web-01", "cpu_usage": 85, "region": "us-east-1"}

for key, value in server.items():
    print(key, ":", value)

# 1. Create a dictionary for a laptop with keys brand, ram, price. Print each key and value using a loop.
dict_laptop= {"Brand" :"HP", "RAM":"16GB", "Price":"$1200"}
for key, value in dict_laptop.items():
    print(key, ":", value)

count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1
      
print("Total even numbers from 1 to 50:", count)