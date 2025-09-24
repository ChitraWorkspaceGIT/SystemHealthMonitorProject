SystemHealthMonitorProject

This project is a Python script that monitors the health of a Linux system.
It checks important system resources like CPU usage, memory usage, disk space, and running processes.
If any resource goes beyond a safe threshold (e.g., CPU > 80%), it logs an alert in the console and in a log file.

Project Setup
1. Create Project Folder

Open VS Code and create a folder named:

SystemHealthMonitor

2. Create Python Script

Inside the folder, create a new file:

system_health_monitor.py


Paste the script into this file.

How to Run

Step 1: Open Terminal in VS Code

Go to Terminal → New Terminal in VS Code.

Step 2: Install Required Package

Psutil is a Python cross-platform library used to access system details and process utilities. It is used to keep track of various resources utilization in the system. Usage of resources like CPU, memory, disks, network, sensors can be monitored. Hence, this library is used for system monitoring, profiling, limiting process resources, and the management of running processes.

The script uses the psutil library. Install it by running:

pip install psutil

Step 3: Run the Script

Execute the script:

python system_health_monitor.py

📝 Logs

When the script runs:

Console Output: Shows system health and alerts.

Log File: system_health.log in the project folder.
Automate on Windows (Task Scheduler)

Press Windows + R, type taskschd.msc, press Enter.

Click Create Basic Task… → Name: System Health Monitor.

Trigger: Daily, set time (e.g., 8:00 AM).

Action: Start a Program

Program/script: Full path to Python:

C:\Users\chint\AppData\Local\Programs\Python\Python312\python.exe


Add arguments: Full path to script:

C:\Users\chint\DOCUMENTS\SystemHealthMonitorProject\system_health_monitor.py


Start in: Folder path only:

C:\Users\chint\DOCUMENTS\SystemHealthMonitorProject


Click Finish.

To test: Right-click → Run. Check system_health.log.

