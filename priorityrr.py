import matplotlib.pyplot as plt

def priority_scheduling(processes, burst_time, arrival_time, priority):
    n = len(processes)
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    current_time = 0
    queue = []
    gantt_chart = []  # Initialize an empty list for the textual Gantt chart

    while True:
        all_done = True
        min_priority_idx = -1  # Initialize with an invalid index

        for i in range(n):
            if remaining_time[i] > 0 and arrival_time[i] <= current_time:
                all_done = False

                if min_priority_idx == -1 or priority[i] < priority[min_priority_idx]:
                    min_priority_idx = i

        if min_priority_idx != -1:
            i = min_priority_idx
            if remaining_time[i] > 0:
                current_time += remaining_time[i]
                completion_time[i] = current_time
                waiting_time[i] = current_time - burst_time[i] - arrival_time[i]
                remaining_time[i] = 0
                turnaround_time[i] = current_time - arrival_time[i]
                queue.append(processes[i])
                gantt_chart.append(processes[i])  # Add the process to the textual Gantt chart
            else:
                gantt_chart.append("Idle")  # Add "Idle" to the textual Gantt chart if no process is scheduled

        if all_done:
            break

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("Process\tArrival Time\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{priority[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    
    ax1.bar(processes, turnaround_time, color='red', label='Turnaround Time')
    ax1.set_xlabel('Processes')
    ax1.set_ylabel('Time')
    ax1.set_title('Turnaround Time for Each Process')
    ax1.legend()

    ax2.bar(processes, waiting_time, color='green', label='Waiting Time', alpha=0.5)
    ax2.set_xlabel('Processes')
    ax2.set_ylabel('Time')
    ax2.set_title('Waiting Time for Each Process')
    ax2.legend()

    ax3.bar(processes, completion_time, color='orange', label='Completion Time', alpha=0.7)
    ax3.set_xlabel('Processes')
    ax3.set_ylabel('Time')
    ax3.set_title('Completion Time for Each Process')
    ax3.legend()

    plt.tight_layout()
    plt.show()

    print("\nTextual Gantt Chart:")
    print(" -> ".join(gantt_chart))

if __name__ == "__main__":
    max_processes = 10

    n = int(input("Enter the number of processes (up to 10): "))
    if n > max_processes:
        print(f"Maximum number of processes allowed is {max_processes}")
        exit(1)

    processes = []
    burst_time = []
    arrival_time = []
    priority = []

    for i in range(n):
        process_name = input(f"Enter the name of process {i + 1}: ")
        arrival = int(input(f"Enter arrival time for process {process_name}: "))
        burst = int(input(f"Enter burst time for process {process_name}: "))
        pri = int(input(f"Enter priority for process {process_name}: "))
        processes.append(process_name)
        arrival_time.append(arrival)
        burst_time.append(burst)
        priority.append(pri)

    priority_scheduling(processes, burst_time, arrival_time, priority)
