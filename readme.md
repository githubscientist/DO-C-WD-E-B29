# Three applications:

    1. The Server Log Analyzer
        - count how many requests came from specific IP addresses
        - count how many 404 or 500 errors occurred
    2. The Automated Backup Script
        - From the source directory, zip all files from that directory and appends the current timestamp to the filename and moves it to a backup directory.
    3. System Health Monitor
        - Checks the hard drive space and raises an alert if the free space is less than 20%

--- Analyzing server.log ---
--- REPORT SUMMARY ---
Total Errors Found: 12

Top Active IPs:
IP: 10.0.0.5 - Requests: 7
IP: 192.168.1.10 - Requests: 5
IP: 45.33.22.11 - Requests: 4
