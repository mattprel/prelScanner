import re
import socket
import subprocess
import sys
from datetime import datetime
import platform
from time import sleep

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

# Format host input
if remoteServer[:7] == "http://":
    remoteServer = remoteServer[7:]
    if remoteServer[-1] == "/":
        remoteServer = remoteServer[:-1]
elif remoteServer[:8] == "https://":
    remoteServer = remoteServer[8:]
    if remoteServer[-1] == "/":
        remoteServer = remoteServer[:-1]
elif remoteServer[-1] == "/":
    remoteServer = remoteServer[:-1]
print(remoteServer)


# Get port from user
remoteServerHost = socket.gethostbyname(remoteServer)
portRange1 = int(input("Specify the lowest port number to scan: "))
portRange2 = int(input("Specify the highest port number to scan: "))
timeoutLength = float(
    input(
        "Please enter the amount of time in seconds before the script gives up connecting to a port (recommended: 0.2): "
    )
)


# Print status messages
print("_" * 60)
print("Please wait, scanning remote host", remoteServerHost)
print("_" * 60)

# Get date and time at start time
t1 = datetime.now()

try:
    for port in range(portRange1, portRange2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeoutLength)
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
input("Press [ENTER] to exit.")
print("Have a nice day!")
sleep(2)
