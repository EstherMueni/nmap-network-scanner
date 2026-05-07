# Nmap Network Scanner

A Python tool that performs network reconnaissance and security 
assessment by scanning target hosts for open ports, running 
services, and potential vulnerabilities.

## What It Does
- Scans target IP or hostname for open ports
- Identifies running services and their versions
- Assesses risk level for each open port
- Generates a clean security report with timestamps

## Skills Demonstrated
- Network reconnaissance and port scanning
- Service identification and version detection
- Risk assessment and security analysis
- Python scripting with external libraries
- Real world application of security concepts

## Tools Used
- Python 3
- Nmap 7.99
- python-nmap library

## How To Run
```bash
python3 scanner.py
```

## Sample Results
Scan of scanme.nmap.org revealed:
- Port 22/SSH - OPEN - Remote access service
- Port 80/HTTP - OPEN - Web server running
- All other scanned ports closed

## Legal Notice
This tool should only be used on systems you own or have 
explicit permission to scan. Practice target used here is 
scanme.nmap.org which is provided by Nmap for legal testing.
