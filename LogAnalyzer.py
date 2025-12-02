class LogAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.errorsCount = 0
        self.activeips = {}

    def analyze(self):
        # Open the file in a read mode
        with open(self.filename, "r") as f:
            # read the contents of the file
            data = f.read()

            # for each line or entry in the file
            for line in data.split('\n'):
                # split the line into multiple parts
                parts = line.split(' ')

                # get each IP address
                ip = parts[0]

                # with each IP address, either make a new entry or update the count of existing entry
                if ip in self.activeips:
                    # the entry is already there
                    # update the entry
                    self.activeips[ip] = self.activeips[ip] + 1
                else:
                    # the entry is not there
                    # make a new entry
                    self.activeips[ip] = 1

                # get the error code or status code
                statusCode = parts[8]

                # if the error code either starts with 4 series or 5 series, then update the error count
                if statusCode.startswith("4") or statusCode.startswith("5"):
                    self.errorsCount = self.errorsCount + 1

    def generateReport(self):
        '''
            --- Analyzing server.log ---
            --- REPORT SUMMARY ---
            Total Errors Found: 12

            Top Active IPs:
            IP: 10.0.0.5 - Requests: 7
            IP: 192.168.1.10 - Requests: 5
            IP: 45.33.22.11 - Requests: 4
        '''
        # print the summary in the given format or structure
        print('--- Analyzing server.log ---')
        print('--- REPORT SUMMARY ---')
        print()
        print('Total Errors Found:', self.errorsCount)
        print()
        print('Top Active IPs:')

        # arrange the ip addresses in descending order based on their requests count
        ipFrequencies = self.activeips.items()

        ipFrequencies = sorted(ipFrequencies, reverse=True, key=lambda x: x[1])

        for key, value in ipFrequencies[0:3]:
            print('IP:', key, '-', 'Requests:', value)


analyzer = LogAnalyzer("server.log")
analyzer.analyze()
analyzer.generateReport()
