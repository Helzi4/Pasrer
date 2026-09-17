with open("python/auth_summary/sample.log", "r") as file:
    logs = file.readlines()
aba = 0
for i in range(len(logs)):
    if "FAILED" in (logs[i]):
        aba = aba + 1
print(f"FAILED:{+aba}")    
      