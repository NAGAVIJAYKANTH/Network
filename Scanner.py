#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple Networking mapping tool")
print("<----------------------------------------------------->")
# Basic user interface header
print(r"""_______    ______     _______      _________
  __          __   _    _    
  \ \        / /  (_)  (_)                 
   \ \      / /    _    _      ___ _    __      __
    \ \    / /    | |  | |   / ___' |  |  |    |  |
     \ \  / /     | |  | |  | /   | |  |  |    |  |
      \ \/ /      | |  | |  | \___| |  |  \__ _/  |
       \__/       |_|  | |   \____,_|   \______,  |
                   __ _/ |              _____ _/  |                      
                  |_ __ _/             |__  __ __/        ***HACKER*** """)
print("\n****************************************************************")
print("\n* Copyright of vijay, 2024 *")
print("\n*Email:nagavijaykanth2001@gmail.com *")
print("\n****************************************************************")


ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")
print("You have selected option: ", resp)
resp_dict = {'1': ['-v -sS', 'tcp'], '2': ['-v -sU', 'udp'], '3': ['-v -sS -sV -sC -A -O', 'tcp']}
if resp not in resp_dict.keys():
    print("Enter a valid option")
else:
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])
# the first argument is the IP address, the second is the port range, and the third is the scan type
    print(scanner.scaninfo())
    if 'status' in scanner[ip_addr] and scanner[ip_addr]['status']['state'] == 'up':
        print("Scanner Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr][resp_dict[resp][1]].keys())  
# display all open ports
