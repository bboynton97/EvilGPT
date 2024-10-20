from ftplib import FTP
from crewai_tools import tool

# FTP server details
ftp_host = 'ftpupload.net'
ftp_user = 'if0_37549272'
ftp_p = 'MBy##D@HNqX3'

@tool("FTP")
def upload_files(file_paths: list[str]):
    """Upload a list of files to the FTP server."""

    result = True
    # Loop through each file path in the list
    for file_path in file_paths:
        # Establish FTP connection
        with FTP(ftp_host) as ftp:
            try:
                # Login to the server
                ftp.login(user=ftp_user, passwd=ftp_p)
                print(f"Connected to FTP server: {ftp_host}")

                # Change to the desired directory on the server
                ftp.cwd(ftp_path)

                # Open the file in binary mode for reading
                with open(file_path, 'rb') as file:
                    # Upload the file
                    ftp.storbinary(f'STOR {file_path}', file)
                    print(f"Successfully uploaded {file_path} to {ftp_path}")

            except Exception as e:
                print(f"An error occurred: {e}")
                result = False

    return result