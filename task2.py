import os
#Task 2: Script that checks if a server is up (using ping)
hostname = "azure"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')