# # bring factorial into this python file
# from math import factorial

# print(factorial(5))

# def factorial(number):
#     result = 1

#     for i in range(1, number+1, 1):
#         result = result * i

#     return result


# print(factorial(5))
def findRunningServers(server_inventory):
    # find the running servers
    # iterate the server inventory
    for server_name in server_inventory:
        if server_inventory[server_name]['status'] == 'Running':
            print(server_inventory[server_name])


server_inventory = {
    "web-01": {
        "ip_address": "192.168.1.10",
        "os": "Ubuntu 22.04",
        "role": "Frontend Web Server",
        "status": "Running"
    },
    "db-01": {
        "ip_address": "192.168.1.20",
        "os": "CentOS 7",
        "role": "PostgresSQL Database",
        "status": "Stopped"
    },
    "jenkins-01": {
        "ip_address": "192.168.1.30",
        "os": "RHEL 9",
        "role": "CI/CD Master",
        "status": "Running"
    }
}

findRunningServers(server_inventory)
