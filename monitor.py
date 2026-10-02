import shutil
import os
import time
import subprocess
GB = 1024 ** 3





def disk():
    total, used, free = shutil.disk_usage("/") 


    print(f"Disk: {used / GB:.1f} GB used of {total / GB:.1f} GB total")

def memory():

    with open("/proc/meminfo") as f:
        for line in f:
            if line.startswith("MemTotal:"):
                total = int(line.split()[1])
            if line.startswith("MemAvailable:"):
                available = int(line.split()[1])
    used = total - available
    print(f"Memory: {used / 1024**2:.1f} GB used of {total / 1024**2:.1f} GB total")


def load_average():

    with open("/proc/loadavg") as f:
        load = f.read().split()
        load_1 = float(load[0])
        cores = os.cpu_count()
        busy = load_1 / cores
    print(f"CPU: {busy:.1%} busy across {cores} cores")

   
while True:
    disk()
    memory()
    load_average()
    time.sleep(2)
    subprocess.run(["clear"])