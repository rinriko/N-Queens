import paramiko

def check_connection(username,password):
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname="willow.cs.ttu.edu", username=username, password=password)
        ftp_client=client.open_sftp()
    except:
        print("[!] Cannot connect to the SSH Server")
        # Close connection
        client.close()
        return(1)
    # Close connection
    ftp_client.close()
    client.close()
    return(0)