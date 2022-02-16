# Title: Check disk space usage, CPU utilization, network connectivty
# Author: Ahmed M Khan
# Date Created: 1/06/22
# Date Modified: 1/06/22
# Description : This scripts checks disk space usage, CPU utilization, network connectivity. It notifies if the thresholds are breached or local host is unable to connect to the network.

#!/usr/bin/env python3
import shutil
import psutil
from network import *

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")