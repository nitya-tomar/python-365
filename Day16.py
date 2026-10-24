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