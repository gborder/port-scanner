import socket
import termcolor

def scan(target, ports):
    print("\n" + " Starting Scan For " + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened: " + str(port))
        sock.close()
    except: 
        pass

targets = input("[*] Enter targets to Scan (Split them by ,): ")
ports = input("[*] Enter amout of ports to Scan: ")
if ',' in targets:
    print(termcolor.colored(("[*] Scaning multiple targets"), 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports) 