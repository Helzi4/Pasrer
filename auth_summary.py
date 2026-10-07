import json
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
parser.add_argument("--threshold", type=int)
args = parser.parse_args()


try: 
    with open(args.file, "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print("NotFoundFile sorry bro")
    sys.exit(1)
fail_by_ip = {}
fail_by_user = {}
for line in logs:
    parts = line.split()
    if len(parts) != 3:
        print("string not correct")
        continue
    ip = parts[0]
    user = parts[1]
    status = parts[2]
    if status == "FAILED":
        if ip in fail_by_ip:
            fail_by_ip[ip] = fail_by_ip[ip] + 1
        else:
            fail_by_ip[ip] = 1
        if user in fail_by_user:
                fail_by_user[user] = fail_by_user[user] + 1
        else:
                fail_by_user[user] = 1
         
         
report = {
    "failed_by_user": fail_by_user,
    "failed_by_ip": fail_by_ip
}

print(json.dumps(report, indent=4))
if args.threshold and args.threshold > 0:
    for user in fail_by_user:
        if fail_by_user[user] >= args.threshold:
            print(((f"{user} have truble") ) )
elif args.threshold == None:
    print("")
else: 
     print("threshold args not correct")                     




       