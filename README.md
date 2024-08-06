 Network Mapping Tool:

  #Overview
   This is a simple network mapping tool built with Python and Nmap. It allows you to perform different types of network scans to identify open ports and services on a target machine.

  #Prerequisites
  - Python 3.x
  - Nmap
  - python-nmap library

  #Installation

  #Python
  Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

  #Nmap
  Download and install Nmap from [nmap.org](https://nmap.org/download.html).

  #python-nmap
  Install the Python wrapper for Nmap using pip:

  pip install python-nmap


 Usage:

 Step-by-Step Instructions:

   1. Save the script `network_mapper.py` in your desired directory.
   2. Open a terminal or command prompt.
   3. Navigate to the directory where `network_mapper.py` is saved.
   4. Run the script using Python:

   python network_mapper.py

   5. Follow the on-screen instructions to enter the IP address and select the type of scan.

  # Script Explanation
   The script prompts the user to enter an IP address and select a scan type:
   1) SYN ACK Scan: Uses the `-v -sS` options for a TCP SYN scan.
   2) UDP Scan: Uses the `-v -sU` options for a UDP scan.
   3) Comprehensive Scan: Uses the `-v -sS -sV -sC -A -O` options for a comprehensive scan.

 #Example:
  ______   _         _     _  ______                 _
  __          __   _    _    
  \ \        / /  (_)  (_)                 
   \ \      / /    _    _      ___ _    __      __
    \ \    / /    | |  | |   / ___' |  |  |    |  |
     \ \  / /     | |  | |  | /   | |  |  |    |  |
      \ \/ /      | |  | |  | \___| |  |  \__ _/  |
       \__/       |_|  | |   \____,_|   \______,  |
                   __ _/ |              _____ _/  |                 
                  |_ __ _/             |__  __ __/                   

  ****************************************************************

  * Copyright of vijay, 2024                              *

  ****************************************************************

  Please enter the ip address that you want to scan: 192.168.1.1
  192.168.1.1 is a valid ip address
  Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)
  Enter port range: 20-25
  Port 20 is closed
  Port 21 is open
  Port 22 is closed
  Port 23 is closed
  Port 24 is closed
  Port 25 is open

 #Outputs
   The script displays the version of Nmap used.
   It shows the scan information and status of the target machine.
   It lists all open ports and protocols found during the scan.
 #License
   This tool is open-source and free to use. Feel free to modify and distribute it as needed.

 #Contact
   For any queries, contact the author:
   Name: Vijay
   Email: nagavijaykanth2001@gmail.com