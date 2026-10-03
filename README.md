# System Monitor

A simple Python program that shows live disk, memory and CPU usage in the terminal, updating every 2 seconds.

```
Disk: 12.6 GB used of 61.7 GB total
Memory: 4.7 GB used of 7.2 GB total
CPU: 18.2% busy across 4 cores
```

## How to run it

Needs Linux and Python 3.

```
python3 monitor.py
```

Press **Ctrl+C** to stop.

## How it works

- **Disk:** uses Python's `shutil.disk_usage()`
- **Memory:** reads Linux's live `/proc/meminfo` file
- **CPU:** reads `/proc/loadavg` and divides by the number of cores

## How I built it

A learning project, written line by line while learning Linux and Python. I built it inside an Ubuntu virtual machine running on my Mac using UTM, coding in VS Code and publishing to GitHub with Git.
