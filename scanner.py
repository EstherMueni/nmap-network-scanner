# Nmap Network Scanner
# Author: Esther
# Description: Scans a target IP for open ports, services,
# and potential security risks

import nmap
import datetime

# Configuration
TARGET = "scanme.nmap.org"  # This is a legal practice target provided by Nmap
PORTS = "22,80,443,3306,8080,21,23,25"

def run_scan(target, ports):
    print(f"\nStarting scan on target: {target}")
    print(f"Scanning ports: {ports}")
    print("Please wait...\n")

    scanner = nmap.PortScanner()
    scanner.scan(target, ports, arguments="-sV")
    return scanner

def generate_report(scanner, target):
    print("="*50)
    print("       NETWORK SECURITY SCAN REPORT")
    print("="*50)
    print(f"Target:     {target}")
    print(f"Scan Time:  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)

    for host in scanner.all_hosts():
        print(f"\nHost: {host}")
        print(f"Status: {scanner[host].state()}")

        print("\nOPEN PORTS & SERVICES:")
        print("-"*40)

        for protocol in scanner[host].all_protocols():
            ports = scanner[host][protocol].keys()

            for port in sorted(ports):
                service = scanner[host][protocol][port]
                state = service["state"]
                name = service["name"]
                version = service["version"]
                product = service["product"]

                if state == "open":
                    print(f"  Port {port}/{protocol}")
                    print(f"  State:   {state.upper()}")
                    print(f"  Service: {name}")
                    if product:
                        print(f"  Product: {product} {version}")
                    print(f"  Risk:    {assess_risk(port)}")
                    print("-"*40)

def assess_risk(port):
    high_risk = [21, 23, 3306]
    medium_risk = [25, 8080]
    low_risk = [80, 443, 22]

    if port in high_risk:
        return "HIGH - This port is commonly exploited"
    elif port in medium_risk:
        return "MEDIUM - Monitor this port closely"
    elif port in low_risk:
        return "LOW - Standard service port"
    else:
        return "UNKNOWN - Investigate further"

def main():
    scanner = run_scan(TARGET, PORTS)
    generate_report(scanner, TARGET)
    print("\nScan complete.")

if __name__ == "__main__":
    main()
