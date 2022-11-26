import nmap

#Enter the IP address and port numbers 
IP_address = input("Enter IP address: ")
port_range = input("Enter in port numbers: ")

#initialize the scans
nmScan = nmap.PortScanner()

#Run the scan
nmScan.scan(IP_address, port_range)

#Print the port results found in the loop
for host in nmScan.all_hosts():
     print('Host: %s (%s)' % (host, nmScan[host].hostname()))
     print('State: %s' % nmScan[host].state())
     for proto in nmScan[host].all_protocols():
         print('----------')
         print('Protocol: %s' % proto)
 
         lport = nmScan[host][proto].keys()
         lport.sort()
         for port in lport:
             print('port: %s\tstate: %s' % (port, nmScan[host][proto][port]['state']))



