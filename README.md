# prelScanner
A simple and easy-to-use port scanner to find vulnerabilities in your network.

## Install Guide
#### Method 1
The easiest way to use this script is to clone it from a Linux terminal or Windows command prompt:
```
git clone https://github.com/mattprel/prelScanner.git
```
Then, change to that directory by using ```cd prelScanner```, and run the script using ```python ./prelScanner.py``` on Windows, or ```python3 ./prelScanner.py``` on Linux.

#### Method 2
Another way to obtain this script is to download it from the releases page, linked [here](https://github.com/mattprel/prelScanner/releases).
After the script has finished downloading, either run it from a GUI or from a terminal/command prompt.

## Usage
After starting the script, you'll see an input for a remote host. Currently, the script is set up to use either an IP address or an FQDN but using an IP address is very highly recommended as using an FQDN has not yet been fully tested and is still extremely buggy. The script will then ask you to enter a starting port and an ending port. Future releases will also allow you to set a timeout, but for now, you'll have to edit **line 36** of the code or use the default timout, which is 0.2 seconds. When the script finishes it will print how long the script took, and then automatically exit.
