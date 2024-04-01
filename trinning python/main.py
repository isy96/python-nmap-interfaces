from try_scan import *
import socket
cl_sc()

interface = get_valid_interfaces()
count = 1
for face in interface:
    print(str(count) + " - " + face)
    count += 1

user = ""
while not user.strip().isdigit() or int(user.strip()) > count:
    user = input("Type interface you want to check: ")

ifaces = interface[int(user.strip()) - 1]
ip_address = get_ip(ifaces)
get_mask_1 = get_mask(ifaces)
scanner = nmap.PortScanner()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("nmap version ", scanner.nmap_version())
print( "name is :", face , "------","IP  scan :" , ip_address)
print("subnet mask is : ",get_mask_1)



user_scanner = input("""
1 - TCP scanner
2 - UDP scanner 
3 - More information \n choose scan : """)



scanner_result = scan_ip(ip_address)
if user_scanner == "1":
    scanner_result = nmap.PortScanner()
    scanner_result.scan(ip_address, '1-340', '-sS')
    print(scanner_result.scaninfo())
    print("IP state:", scanner_result[ip_address].state())
    print("All protocols:", scanner_result[ip_address].all_protocols())
    print("Open TCP ports:", scanner_result[ip_address]['tcp'].keys())

elif user_scanner == '2':
    scanner_result = nmap.PortScanner()
    scanner_result.scan(ip_address, '1-800', '-sU')
    print(scanner_result.scaninfo())
    print("IP state:", scanner_result[ip_address].state())
    print("All protocols:", scanner_result[ip_address].all_protocols())
    print("Open UDP ports:", scanner_result[ip_address]['udp'].keys())

elif user_scanner == '3':
    scanner_result = nmap.PortScanner()
    scanner_result.scan(ip_address, '1-800', '-sS -sV -A -sC -O')
    print(scanner_result.scaninfo())
    print("IP state:", scanner_result[ip_address].state())
    print("All protocols:", scanner_result[ip_address].all_protocols())
    print("Open TCP ports:", scanner_result[ip_address]['tcp'].keys())

else:
    TypeError("enter valid number")
    