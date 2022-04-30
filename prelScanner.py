import socket
import subprocess
import sys
from datetime import datetime
import platform

os = platform.system()

platform.system()

if os == "Linux":
    # Clear screen
    subprocess.call("clear", shell=True)
elif os == "Windows":
    # Clear screen
    subprocess.call("cls", shell=True)


# Get host from user
remoteServer = input("Enter a remote host to scan: ")
remoteServerHost = socket.gethostbyname(remoteServer)
portRange1 = int(input("Specify the lowest port number to scan: "))
portRange2 = int(input("Specify the highest port number to scan: "))

# Print status messages
print("_" * 60)
print("Please wait, scanning remote host", remoteServerHost)
print("_" * 60)

# Get date and time at start time
t1 = datetime.now()

try:
    for port in range(portRange1, portRange2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((remoteServerHost, port))
        if result == 0:
            print("Port {}:    Open".format(port))
        else:
            print("Port {}:    Closed".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Ctrl+C pressed, exiting now. Thank you for using this script!")
    sys.exit()

except socket.gaierror:
    print("Resolving the hostname failed, restart the script to try again. Exiting.")

except socket.error:
    print("Connecting to the server failed. Exiting.")

# Get date and time at end time
t2 = datetime.now()

elapsedTime = t2 - t1

print("Scanning Complete! ", "The total time to complete the scan was:", elapsedTime)
