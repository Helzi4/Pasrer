import argparse
import sys
import json

def parse_line(line):
    part = line.split()
    if part == []:
            return None
    if len(part) < 8:
        print("line not correct")
        return None
    ip = part[0]
    status = part[7]
    path = part[5]
    method = part[4].strip('"')

    result = {
        "ip": ip,
        "status": status,
        "path": path,
        "method": method
    }
    return result

def count(parametr, count):
    if parametr in count:
        count[parametr] = count[parametr] + 1
    else:
        count[parametr] = 1   

def aler(suspicious_ips, threshold):
    aler_p = {}
    if threshold and threshold > 0: 
            for ip, failed_req in suspicious_ips.items():
                if failed_req >= threshold:
                    aler_p[ip] = failed_req
            return aler_p       

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--threshold", type=int, default=3)
    args = parser.parse_args()            

    try:
        with open(args.file) as file:
            log = file.readlines()
    except FileNotFoundError:
        print("Not correct bro, i'm don't see the file")          
        sys.exit(1)

    total_request = 0
    ips = {}
    statuses = {}
    top_paths = {}
    methods = {}
    suspicious_ips = {}

    
    for line in log:
        returned_data = parse_line(line)
        if returned_data == None:
            continue
        total_request = total_request + 1
        ip = returned_data["ip"]
        status = returned_data["status"]
        path = returned_data["path"]
        method = returned_data["method"]
        #-----------------------------------------------------------
        count(ip,ips)

        count(status, statuses)

        count(path, top_paths)

        count(method, methods)                      
        #-------------------------------------------------------------------
                
        if status == "401" or status == "403":
            count(ip, suspicious_ips)                         
            
    aler_result = aler(suspicious_ips, args.threshold)



    final = {
    "total_request": total_request,
    "status_codes": statuses,
    "methods": methods,
    "top_ips": ips,
    "top_path": top_paths,
    "suspicious_ips": suspicious_ips,
    "alerts_ip": aler_result
    
            }

    print(json.dumps(final, indent=4))   
    

if __name__ == "__main__":
    main()    