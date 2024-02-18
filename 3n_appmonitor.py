import psutil
import subprocess
import time

def count_running_instances(app_name):
    count = 0
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == app_name:
            count += 1
    return count

def close_application(app_name, pid):
    subprocess.call(['taskkill', '/F', '/PID', str(pid)])

def monitor_applications():
    app_names = ['chrome.exe', 'msedge.exe', 'Teams.exe', 'calc.exe', 'notepad.exe']
    max_instances = 2

    while True:
        for app_name in app_names:
            running_instances = count_running_instances(app_name)
            if running_instances > max_instances:
                print(f"Warning: {running_instances} instances of {app_name} detected.")
                instances_to_close = running_instances - max_instances
                closed_count = 0
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] == app_name:
                        close_application(app_name, proc.info['pid'])
                        closed_count += 1
                        if closed_count >= instances_to_close:
                            break
            else:
                print(f"{running_instances} instances of {app_name} running.")

        # Delay for a few seconds between each check
        time.sleep(5)

monitor_applications()