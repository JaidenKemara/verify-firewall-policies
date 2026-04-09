# verify-firewall-policies
This script verifies specific firewall policies by attempting connections to scanme.nmap.org on specified ports. For example, if you have policies allowing or denying TCP connections on port 22, this script will indicate whether or not the connection attempt was successful. 


Example output when ports are allowed:

<img width="596" height="313" alt="image" src="https://github.com/user-attachments/assets/dd9483aa-1752-4ed7-9f8b-0c0b5fd21d9b" />


Example output when a port is blocked (in this case port 22):

<img width="477" height="237" alt="image" src="https://github.com/user-attachments/assets/e9d41ff3-b68a-4423-b90d-7076edcd98ec" />
