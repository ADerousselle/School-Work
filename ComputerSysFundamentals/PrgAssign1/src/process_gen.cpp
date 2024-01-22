#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

/* Process struct
	Holds the data for each process including its...
	id: The placement of the process in the list of all processes.
	arrival_time: The actual time that the process is recieved by the server.
	service_time: The actual time that the process takes to be serviced.
*/
struct Process {
	int id;
	double arrival_time;
	double service_time;
};

/* rand_expo(rate)
	Gets a random exponential number based on a given rate.
*/
double rand_expo(double rate) {
	return -log(1.0 - static_cast<double>(rand())/RAND_MAX) / rate;
}

/* process_gen(processes_len)
	Creates a vector of processes that are serviced by the server. Each element of the
	vector contains a process id, arrival time, and service time. 
	processes_len: The length of the processes vector, with a default value of 1000.
*/

int main() {
	//A variable indicating the number of processes to generate.
	int processes_len = 1000;

	// Seeds the random number generator so that each run of the program produces
	// different results (for realism).
	//srand(static_cast<unsigned int>(time(nullptr)));

	// Predefined variables giving the expected arrival rate and expected service rate.
	double exp_arrival_rate = 2.0;
	double exp_service_rate = 1.0;
	// A vector to hold the Process elements.
	vector<Process> processes;
	// A variable to keep track of the time taken to receive all processes.
	double current_time = 0;
	// Counter to assign an id to each process.
	int process_id = 1;
	// An accumulator to keep track of the total time spent servicing the processes.
	double sum_service_time = 0;

	//A while loop that creates each process, determines it's values, and adds it to
	//the processes vector
	for(process_id; process_id <= processes_len; process_id++) {
		//A variable determined at random by the expected arrival rate, that holds
		//the value of time between one processes arrival and the previous' arrival.
		double interarrival_time = rand_expo(exp_arrival_rate);
		//A variable determined at random by the expected service rate, that holds
		//the value of time needed to service a particular process.
		double req_service_time = rand_expo(exp_service_rate);
		//Determine the current time and thus the arrival time of the current process
		//by adding the interarrival_time to the previous current_time.
		current_time += interarrival_time;
		//Create the process as a list of values and push it onto the processes
		//vector.
		processes.push_back({process_id, current_time, req_service_time});
		//add the current process's service time to the sum of service times.
		sum_service_time += req_service_time;
	}

	//A variable indicating the actual average arrival rate of a process.
	double act_arrival_rate = processes_len / current_time;
	//A variable indicating the actual average service time of a process.
	double act_service_time = sum_service_time / processes_len;

	//Print the act_arrival_rate, act_service_time, and the list of processes to a file.
	ofstream file("output/process_gen_out.txt");
	if (file.is_open()) {
		file << "Actual Average Arrival Rate: " << act_arrival_rate << endl;
		file << "Actual Average Service Time: " << act_service_time << endl;
		file << processes_len << " Processes" << endl;;
		for (const Process& process : processes) {
			file << process.id << " " << process.arrival_time << " " << process.service_time << endl;
		}
		file.close();
	}
	else {
		cout << "Unable to open file for writing." << endl;
	}
	return 0;
}

