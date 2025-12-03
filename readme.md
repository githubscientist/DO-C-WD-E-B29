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

total = 245107195904 bytes
used = 214783844352 bytes
free = 30323351552 bytes

1024 bytes = 1 Kilo Byte
1024 Kilo Bytes = 1 Mega Byte
1024 Mega Bytes = 1 Giga Byte

1024 = 2 \* 10

total = 245107195904 bytes = 245107195904 / 2^30 = 228.3 Giga Bytes
used = 214783844352 bytes = 214783844352 / 2^30 = 199.9 Giga Bytes
free = 30323351552 bytes = 30323351552 / 2^30 = 28.2 Giga Bytes

used space percentage = (used / total) _ 100 = (199.9 / 228.3) _ 100 = 87.5 %
free space percentage = (free / total) _ 100 = (28.2 / 228.3) _ 100 = 12.5 %
