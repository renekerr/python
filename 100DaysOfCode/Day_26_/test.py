existing_servers = ['server01', 'server02', 'server03', 'server04']
active_directory_ou_servers = ['server01', 'server02', 'server03', 'server04', 'server05', 'server06', 'server07']
unregistered_servers = [item for item in active_directory_ou_servers if item not in existing_servers]

print(unregistered_servers)
