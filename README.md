import time
from datetime import datetime as dt
import os

sites_to_block = [
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com",
    "www.gmail.com", "gmail.com"
]

redirect = "127.0.0.1"

# OS-specific hosts path
if os.name == 'posix':
    hosts_path = "/etc/hosts"
elif os.name == 'nt':
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    print("OS Unknown")
    exit()

def block_websites(start_hour, end_hour):
    while True:
        try:
            now = dt.now()
            if dt(now.year, now.month, now.day, start_hour) < now < dt(now.year, now.month, now.day, end_hour):
                print("Blocking sites...")
                with open(hosts_path, "r+") as file:
                    hosts = file.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            file.write(redirect + " " + site + "\n")
            else:
                print("Unblocking sites...")
                with open(hosts_path, "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    for line in lines:
                        if not any(site in line for site in sites_to_block):
                            file.write(line)
                    file.truncate()
            time.sleep(60)  # check every 1 minute
        except PermissionError:
            print("Permission denied: Run as Admin/Root")
            break

if __name__ == "__main__":
    block_websites(9, 21)
