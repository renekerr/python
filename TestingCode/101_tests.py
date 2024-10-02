import pyodbc

# Define the new_servers and full_info lists
new_servers = ['server1', 'server2', 'server3', 'server4']
full_info = [
    ['server1', 'Alex', 'alex@email.com'],
    ['server2', 'Albert', 'albert@email.com'],
    ['server3', 'Alice', 'alice@email.com'],
    ['server4', 'Amanda', 'amanda@email.com']
]

# Create an empty list to store the final output
output_info = []

# Loop through each server in full_info and get the required details
for server, name, email in full_info:
    # Define the connection string
    conn_str = f"Driver={{SQL Server}};Server={server};Trusted_Connection=yes;"

    conn = None  # Initialize the connection variable
    try:
        # Connect to the SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Get the SQL Server version
        cursor.execute("SELECT @@VERSION")
        sql_version_full = cursor.fetchone()[0]

        # Extract the concise version using split
        sql_version = "SQL Server " + sql_version_full.split()[
            3] if "Microsoft SQL Server" in sql_version_full else "Unknown SQL Server version"

        # Determine if the server is part of a cluster or stand-alone
        cursor.execute("SELECT SERVERPROPERTY('IsClustered')")
        is_clustered = cursor.fetchone()[0]
        cluster_status = 'HADR' if is_clustered else 'SA'

        # Get the list of user databases
        cursor.execute("SELECT name FROM sys.databases WHERE owner_sid != 0x01")
        user_databases = [row[0] for row in cursor.fetchall()]

        # If no user databases found, add a default message
        if not user_databases:
            user_databases = ['No user database found']

        # Append the information to the output list
        output_info.extend([[server, db, name, email, sql_version, cluster_status] for db in user_databases])

    except Exception as e:
        print(f"Failed to connect to {server}: {e}")
        # In case of connection failure, add a message to the output
        output_info.append([server, 'Connection failed', name, email, 'Unknown version', 'Unknown status'])

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

# Print the results in the desired format
for info in output_info:
    print(', '.join(info))

# Print the INSERT commands
for info in output_info:
    server, db, name, email, sql_version, cluster_status = info
    insert_command = (
        f"INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) "
        f"VALUES ('{server}', '{db}', '{name}', '{email}', '{sql_version}', '{cluster_status}');"
    )
    print(insert_command)

"""
sample results
server1, db1, Alex, alex@email.com, SQL Server 2019, SA
server1, db2, Alex, alex@email.com, SQL Server 2019, SA
server2, db1, Albert, albert@email.com, SQL Server 2022, HADR
server2, db2, Albert, albert@email.com, SQL Server 2022, HADR
server3, No user database found, Alice, alice@email.com, SQL Server 2017, SA
server4, No user database found, Amanda, amanda@email.com, SQL Server 2019, HADR

INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) VALUES ('server1', 'db1', 'Alex', 'alex@email.com', 'SQL Server 2019', 'SA');
INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) VALUES ('server1', 'db2', 'Alex', 'alex@email.com', 'SQL Server 2019', 'SA');
INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) VALUES ('server2', 'db1', 'Albert', 'albert@email.com', 'SQL Server 2022', 'HADR');
INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) VALUES ('server2', 'db2', 'Albert', 'albert@email.com', 'SQL Server 2022', 'HADR');
INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) VALUES ('server3', 'No user database found', 'Alice', 'alice@email.com', 'SQL Server 2017', 'SA');
INSERT INTO server_info (server, database, name, email, sql_version, cluster_status) VALUES ('server4', 'No user database found', 'Amanda', 'amanda@email.com', 'SQL Server 2019', 'HADR');

"""