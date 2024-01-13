#Imports
import queue
import random
import math
import sys

#Main function
def main(arr_rate, serv_time):
    #Initialization
    processes = 0                                          #current number of processes that have been completed
    proc_max = 10000                                       #total number of processes that may be completed
    eventQ = queue.PriorityQueue()                         #a queue of events that have not yet arrived in the system
    readyQ = queue.PriorityQueue()                         #a queue of arrival events (processes) waiting to be serviced by the CPU
    idle = True                                            #boolean describing whether or not the CPU is currently serving a process
    curr_proc_arr = 0                                      #the arrival time of the process currently being serviced by the CPU
    turnaround_sum = 0                                     #sum of all turnaround times
    clock = 0                                              #the current time
    busy_time_start = 0                                    #the time at which the CPU became busy (idle changed from true to false)
    tot_busy_time = 0                                      #sum of all time that the CPU was busy
    readyQ_count_sum = 0                                   #sum of all processes waiting to be serviced by the CPU during each iteration of the loop

    #Start off the eventQ
    time = clock + interarr_rate(arr_rate)                #calculate a random arrival time
    eventQ.put((time, "ARR"))                             #create and enqueue a arrival event into the eventQ

    #Loop to generate 10,000 processes and process events
    while processes < proc_max and not eventQ.empty():    #While we have not reached the max number of processes and the eventQ is not empty
        e = eventQ.get()                                  #Get the next event and save it in variable e
        clock = e[0]                                      #Set the current time to the time of e
        
        if e[1] == "ARR":                                 #If e is an arrival event
            if idle:                                          #If the CPU is idle
                curr_proc_arr = e[0]                              #Save the current events arrival time
                time = clock + req_serv_time(serv_time)           #calculate a random service time
                eventQ.put((time, "DEP"))                         #create and enqueue a departure event into the eventQ
                idle = False                                      #Set idle to false
                busy_time_start = clock                           #Save the time at which the CPU became busy
            else:                                             #If the CPU is not idle
                readyQ.put(e)                                     #Put the event into the readyQ
            time = clock + interarr_rate(arr_rate)            #calculate a random arrival time
            eventQ.put((time, "ARR"))                         #create and enqueue a arrival event into the eventQ
            
        elif e[1] == "DEP":                               #If e is a departure event
            if not readyQ.empty():                            #If readyQ is not empty
                turnaround_sum += e[0] - curr_proc_arr            #Calculate the turnaround time of the current process being serviced by the CPU and add it to the turnaround_sum
                time = clock + req_serv_time(serv_time)           #calculate a random service time
                if(processes == proc_max - 1):                    #If this is the last process to be completed
                    tot_busy_time += e[0] - busy_time_start           #calculate the time the CPU was busy and add it to the tot_busy_time
                e = readyQ.get()                                  #Get the next process from the readyQ
                curr_proc_arr = e[0]                              #Save the current events arrival time
                eventQ.put((time, "DEP"))                         #create and enqueue a departure event into the eventQ
            else:                                             #If readyQ is empty
                idle = True                                       #Set idle to true
                tot_busy_time += e[0] - busy_time_start           #calculate the time the CPU was busy and add it to the tot_busy_time
                turnaround_sum += e[0] - curr_proc_arr            #calculate the turnaround time of the current process being serviced by the CPU and add it to the turnaround_sum
            processes += 1                                    #Increment the number of processes completed
        readyQ_count_sum += readyQ.qsize()                #Increment the readyQ_count_sum by the number of events currently in readyQ

    #Print the metrics of the simulation
    print_metrics(turnaround_sum, processes, clock, tot_busy_time, readyQ_count_sum) 

def interarr_rate(arr_rate):
    return (-math.log(1 - random.random()) / arr_rate)

def req_serv_time(serv_time):
    return (-math.log(1 - random.random()) * serv_time)

def print_metrics(turnaround_sum, processes, clock, tot_busy_time, readyQ_count_sum):   
    avg_turn_time = turnaround_sum / processes
    tot_throughput = processes / clock
    avg_CPU_util = (tot_busy_time / clock) * 100
    avg_readyQ_count = readyQ_count_sum / clock

    print(f"Average Turnaround Time: {round(avg_turn_time, 4)} seconds")
    print(f"Total Throughput: {round(tot_throughput, 4)} processes per second")
    print(f"Average CPU Utilization: {round(avg_CPU_util, 4)}%")
    print(f"Average Ready Queue Count: {round(avg_readyQ_count, 4)} processes")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py arrival_rate service_time")
    else:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        arr_rate = int(arg1)
        serv_time = float(arg2)
        main(arr_rate, serv_time)