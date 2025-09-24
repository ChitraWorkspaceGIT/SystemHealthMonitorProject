#!/usr/bin/env python3
# Beginner-friendly System Health Monitor

import psutil
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 300

LOG_FILE = "system_health.log"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} - {message}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

# CPU
cpu = psutil.cpu_percent(interval=1)
if cpu > CPU_THRESHOLD:
    log_message(f"ALERT: High CPU usage: {cpu}%")
else:
    log_message(f"CPU usage: {cpu}%")

# Memory
mem = psutil.virtual_memory()
if mem.percent > MEM_THRESHOLD:
    log_message(f"ALERT: High Memory usage: {mem.percent}%")
else:
    log_message(f"Memory usage: {mem.percent}%")

# Disk
disk = psutil.disk_usage('/')
if disk.percent > DISK_THRESHOLD:
    log_message(f"ALERT: High Disk usage: {disk.percent}%")
else:
    log_message(f"Disk usage: {disk.percent}%")

# Processes
process_count = len(psutil.pids())
if process_count > PROCESS_THRESHOLD:
    log_message(f"ALERT: Too many processes: {process_count}")
else:
    log_message(f"Running processes: {process_count}")

log_message("Health check completed.\n")
