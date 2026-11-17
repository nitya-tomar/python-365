text = "  Disk usage high on web-03  "

# 3. check kar "web-03" text ke andar hai ya nahi, True/False print kar
if text.find("web-03") != -1:
    print(True)

# 1. strip karke print kar

text1=text.strip( )
print(text1)

# 2. uppercase mein print kar
text2=text1.upper()
print(text2)

    
    
# 4. "high" ko "critical" se replace karke print kar
t1 = text1.replace("high","critical")
print(t1)

logs = [
    "2026-10-24,web-01,INFO,Started",
    "2026-10-24,web-02,ERROR,Disk Full",
    "2026-10-24,web-03,WARN,High CPU",
    "2026-10-24,web-04,ERROR,Connection Timeout"
]

# Har line ko split(",") kar
for i in logs:
    logs1=i.split(",")
    if logs1[2] == "ERROR":
        print(f"{logs1[1]} - {logs1[3]}")
# Agar level (index 2) "ERROR" hai, to print kar: server name aur message
# Expected output:
# web-02 - Disk Full
# web-04 - Connection Timeout