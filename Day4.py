#Numbers 1-100 divisible by both 3 and 5
for i in range (1,101) :
    if i % 3 ==0 and i % 5==0 :
        print(i)
 #(zombie key check)
        
keys = {"key1": 45, "key2": 120, "key3": 200}
for k , v in keys.items():
    if v>90:
        print(f"Zombie key detected in : {k}")