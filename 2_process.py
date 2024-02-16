# II. Write a Program 
# 1. to find all the list of all running process in your System
# 2. Display the count of each running process.
# 3. Store this information in a CSV File.
                                        
import psutil
import csv

def get_running_processes():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_list.append({'pid': proc.info['pid'], 'name': proc.info['name']})
    return process_list

def count_processes(process_list):
    process_counts = {}
    for process in process_list:
        name = process['name']
        if name in process_counts:
            process_counts[name] += 1
        else:
            process_counts[name] = 1
    return process_counts

def store_process_info_csv(process_list, process_counts):
    with open('process_info.csv', 'w', newline='') as csvfile:
        fieldnames = ['PID', 'Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for process in process_list:
            name = process['name']
            pid = process['pid']
            count = process_counts[name]
            writer.writerow({'PID': pid, 'Name': name, 'Count': count})

# Get the list of running processes
running_processes = get_running_processes()

# Count the processes
process_counts = count_processes(running_processes)

# Display the count of each running process
for name, count in process_counts.items():
    print(f"{name}: {count}")

# Store the process information in a CSV file
store_process_info_csv(running_processes, process_counts)