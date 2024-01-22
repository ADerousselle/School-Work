#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>

using namespace std;

/*Function that does the work for solving problem a or problem b. Both problems have shared
variables that are initiated in at the beginning and then the rest of the function is divided
into two parts, one to solve each problem.
*/
void server_fail(string part, int sims){
	//Mean Time Before Failure, the average time between a successful restore and
	//a failure
	int mtbf = 500;
	//The amount of time it takes for a server to restore itself after a failure
	int restore = 10;
	//Variables to hold the failure and restore points for server 1 and...
	int s1f, s1r = 0;
	//...server 2
	int s2f, s2r = 0;
	//Variables to hold the current time for each server, since they won't necessarily
	//be failing at the same time.
	int time_s1, time_s2 = 0;

	//Section for solving part a.
	if(part == "a"){
		//Variable indicating the total number of years we want to generate processes
		//during for server 1 and 2.
		int yrs = 20;
		//Two vectors, one for each server, that holds the failure time and restore
		//time for each time a server fails (called an event).
		vector<pair<int, int>> s1t, s2t;
		//Variable indicating the yrs in terms of hours.
		int duration = yrs * 365 * 24;

		//While either server has not finished generating failures and restores
		//within the alloted time.
		while(time_s1 < duration || time_s2 < duration){
			//If both have finished generating failures and restores then exit
			//the loop.
			if(time_s1 >= duration && time_s2 >= duration){
				break;
			}
			//Generate the time to the next failures for both servers.
			s1f = -mtbf * log(1.0 - static_cast<double>(rand())/RAND_MAX);
			s2f = -mtbf * log(1.0 - static_cast<double>(rand())/RAND_MAX);
			//Add the time to the next failure to the current time for each
			//server to get the current time as well as the time for the failure.
			time_s1 += s1f;
			time_s2 += s2f;
			//If server 1 has not finished generating failures in the alloted
			//time.
			if(time_s1 < duration){
				//Calculate the time in which the restoration is complete, by
				//adding restore to the current time.
				s1r = time_s1 + restore;
				//Add the failure and restore event to the server 1 vector.
				s1t.push_back(make_pair(time_s1, s1r));
			}
			//If server 2 has not finished generating failures in the alloted
			//time.
			if(time_s2 < duration){
				//Calculate the time in which the restoration is complete, by
				//adding restore to the current time.
				s2r = time_s2 + restore;
				//Add the failure and restore event to the server 2 vector.
				s2t.push_back(make_pair(time_s2, s2r));
			}
		}
		//Print the Server 1 and 2 event vectors.
		ofstream file("output/server_fail_a_out.txt");
		if(file.is_open()){
			file << "Server 1 Failure and Restore Times:" << endl;
			for(const auto& event : s1t){
				file << event.first<< " " << event.second << endl;
			}
			file << "Server 2 Failure and Restore Times:" << endl;
			for(const auto& event : s2t){
				file << event.first << " " << event.second << endl;
			}
			file.close();
		}
		else{
			cout << "Unable to open file for writing." << endl;
		}
	}
	//Section to solve part b.
	else if (part == "b"){
		//Variable to accumulate the total time until a total system failure occurs
		//for all sims.
		int total_failure_time = 0;
		//A vector to hold a list of the times of failure events.
		vector<int> failure_times;

		//For sims times.
		for(int i = 0; i < sims; i++){
			//set all failure, restore, and current times to 0
			s1f = s1r = s2f = s2r = 0;
			time_s1 = time_s2 = 0;
			//Set the random number generator to pick a new seed (based on i).
			srand(static_cast<unsigned int>(time(nullptr))+i);
			//While a total system failure has not occured.
			while(true){
				//Calculate the time to the next failure for server 1 and 2.
				s1f = -mtbf * log(1.0 - static_cast<double>(rand())/RAND_MAX);
				s2f = -mtbf * log(1.0 - static_cast<double>(rand())/RAND_MAX);
				//Calculate the current and failure time for server 1 and 2.
				time_s1 += s1f;
				time_s2 += s2f;
				//if a total server failure has occured...
				if((time_s1 >= time_s2 && time_s1 - restore <= time_s2) ||
				   (time_s2 >= time_s1 && time_s2 - restore <= time_s2)){
					//...add the the time of the event to the
					//total_failure_time,...
					total_failure_time += max(time_s1, time_s2);
					//...add the time of the failure to the
					//failure_times vector, and...
					failure_times.push_back(max(time_s1, time_s2));
					//exit the loop.
					break;
				}
			}
		}
		//Once all sims have been completed, calculate the average time it takes
		//until a total system failure.
		double avg_failure_time = static_cast<double>(total_failure_time) / sims;

		//Print the average time until a total system failure, and the list of
		//event times to a file.
		ofstream file("output/server_fail_b_out.txt");
		if(file.is_open()){
			file << "Average Time Until Total System Failure: " << avg_failure_time << endl;
			for(const auto& failure : failure_times){
				file << failure << endl;
			}
			file.close();
		}
		else{
			cout << "Unable to open file for writing." << endl;
		}
	}
}

/*Main function which accepts command line arguments that indicate which 
probelm to solve as well as how many simulations to run for problem b.
*/
int main(int argc, char* argv[]){
	//Populates rand() with different seeds everytime the program 
	//is run. For realism.
	//srand(static_cast<unsigned int>(time(nullptr)));

	//Default values
	//String variable indicating which part of the problem to solve, values are a or b.
	string part = "a";
	//Integer variable indicating how many simulations to run for problem b.
	int sims = 500;

	//Accepts command line arguments based on how many are entered.
	if(argc >= 2){
		part = argv[1];
	}
	if(argc >= 3){
		sims = atoi(argv[2]);
		if(sims > 500){
			cout << "Please use a number less than or equal to 500." << endl;
			return 1;
		}

	}

	//Calls the functions that solves the problems.
	server_fail(part, sims);

	return 0;
}
