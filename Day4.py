#Numbers 1-100 divisible by both 3 and 5
for i in range (1,101) :
    if i % 3 ==0 and i % 5==0 :
        print(i)
 #(zombie key check)
        
keys = {"key1": 45, "key2": 120, "key3": 200}
for k , v in keys.items():
    if v>90:
        print(f"Zombie key detected in : {k}")
    else:
        print(f"{k} is active")

   

region_status = {"us-east-1": "healthy", "us-west-2": "degraded", "ap-south-1": "healthy"}
# print only regions that are "degraded"
for region, status in region_status.items():
    if status == "degraded":
        print(f"Region {region} is degraded")   
    else:
        print(f"Region {region} is healthy")


# print "Pass" if marks >= 40, else "Fail"
student = {"name": "Nitya", "marks": 82}
if student["marks"] >= 40:
    print("Pass")
else:
    print("Fail")