BCK_RET_DAYS = 15
server_name_list = ['SRNAMESQLE2', 'SRNAMESQLD01', 'SRNAMESQLP1', 'SRNAMESQLE02']


def get_environment(server_name):
    suffix_segment = server_name[-3:]
    environment_label = ''
    suffix_to_environment = {
        'D': 'DES',
        'P': 'PRE',
        'E': 'PRO'
    }

    for suffix in suffix_to_environment:
        if suffix in suffix_segment:
            environment_label = suffix_to_environment[suffix]
            break
    return environment_label


# Iterate over the list of server names and get the environment for each
environments = [get_environment(server_name) for server_name in server_name_list]

# Print the results
for server_name, environment in zip(server_name_list, environments):
    print(f'{server_name}: {environment}')

"""
server_name = 'SRNAMESQLE2'


def get_environment(server):
    suffix_segment = server[-3:].upper()
    environment_code = ''
    suffix_to_environment = {
        'D': 'DES',
        'P': 'PRE',
        'E': 'PRO'
    }

    for suffix in suffix_to_environment:
        if suffix in suffix_segment:
            environment_code = suffix_to_environment[suffix]
    return environment_code


env_output = get_environment(server=server_name)
print(env_output)
"""
