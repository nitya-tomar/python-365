#functions - for checking cpu usage

def check_cpu(server_name, usage):
    if usage > 80:
        print(server_name, "- ALERT")
    else:
        print(server_name, "- OK")

check_cpu("web-01", 92)
check_cpu("web-02", 45)
check_cpu("web-03", 78)

#----------------------------------------for finding unused keys
def is_zombie(days_unused):
    if days_unused > 90:
        return True
    else:
        return False

result = is_zombie(120)
print(result)   # True

result2 = is_zombie(30)
print(result2)  # False