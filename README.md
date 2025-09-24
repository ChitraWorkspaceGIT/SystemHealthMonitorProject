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

The script uses the psutil library. Install it by running:

pip install psutil

Step 3: Run the Script

Execute the script:

python system_health_monitor.py

📝 Logs

When you run the script:

You’ll see alerts in the console.

A log file named system_health.log will be created in your folder with all reports.
