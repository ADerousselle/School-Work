Author: Abigail Derousselle
Date: 10/30/2023
Programming Assignment 2

-------------------------------------------------------------------------------------------

Program Name:
	eventSim.py
Purpose:
	A discrete-time event simulator for a First-Come First-Served CPU scheduling 	algorithm. It is meant to print metrics describing the impact of a workload 	defined by the user.
 
How To Use:
	1. Go to the location you have eventSim.py 
	2. Compilation and Execution
		The program expects two arguments:
			average arrival rate (arr_rate)
			average service time (serv_time)
		In the command line enter the following command with arr_rate and 			serv_time filled in with the your values:
			"python eventSim.py arr_rate serv_time"
	4. Viewing Results
		Results will be printed on terminal after the line compilation and 			execution line you entered.
Understanding the Output:
	The Results consist of four metrics each on their own line 
	1. Average Turnaround Time
		This metric describes the average amount of time (seconds) it takes a 			process to arrive then exit a system.
	2. Total Throughput
		This metric describes the total number of processes that are completed 			per unit of time (seconds).
	3. Average CPU Utilization
		This metric describes the percent of time that the CPU was busy 			completeing processes.
	4. Average Ready Queue Count
		This metric describes the average number of processes waiting to be 			executed by the CPU.