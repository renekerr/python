new_servers = ['server1', 'server2']
server_responsible = ['Alex', 'alex@email.com', 'Albert', 'alber@email.com']
full_info = [[server, server_responsible[i], server_responsible[i + 1]] for i, server in
             enumerate(new_servers)]
print(full_info)
