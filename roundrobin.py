import matplotlib.pyplot as plt

def round_robin(processes, burst_time, arrival_time, quantum):
    n = len(processes)
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    queue = []

    while True:
        all_done = True

        for i in range(n):
            if remaining_time[i] > 0 and arrival_time[i] <= current_time:
                all_done = False

                if remaining_time[i] > quantum:
                    current_time += quantum
                    remaining_time[i] -= quantum
                else:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - burst_time[i] - arrival_time[i]
                    remaining_time[i] = 0
                    turnaround_time[i] = current_time - arrival_time[i]

                queue.append(processes[i])

        if all_done:
            break

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
    
    print("\nTextual Gantt Chart:")
    for process in queue:
        process_idx = processes.index(process)
        print(f"{processes[process_idx]:^3}", end=" ")
    print()

    # Create subplots for the bar graphs of waiting time and turnaround time
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

    ax1.bar(processes, waiting_time, color='green', label='Waiting Time')
    ax1.set_xlabel('Processes')
    ax1.set_ylabel('Time')
    ax1.set_title('Waiting Time for Each Process')
    ax1.legend()

    ax2.bar(processes, turnaround_time, color='blue', label='Turnaround Time')
    ax2.set_xlabel('Processes')
    ax2.set_ylabel('Time')
    ax2.set_title('Turnaround Time for Each Process')
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    max_processes = 10

    n = int(input("Enter the number of processes (up to 10): "))
    if n > max_processes:
        print(f"Maximum number of processes allowed is {max_processes}")
        exit(1)

    processes = []
    burst_time = []
    arrival_time = []

    for i in range(n):
        process_name = input(f"Enter the name of process {i + 1}: ")
        arrival = int(input(f"Enter arrival time for process {process_name}: "))
        burst = int(input(f"Enter burst time for process {process_name}: "))
        processes.append(process_name)
        arrival_time.append(arrival)
        burst_time.append(burst)

    quantum = int(input("Enter time quantum: "))
    round_robin(processes, burst_time, arrival_time, quantum)
