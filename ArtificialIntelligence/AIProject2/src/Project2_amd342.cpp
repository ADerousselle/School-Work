using namespace std;
#include "Puzzle_Tree.h"
#include "Puzzle_Tree.cpp"
#include <iostream>
#include <fstream>
#include <filesystem>

int main(){
    //pointer to a Puzzle_Tree object, which produces a tree and prints out metric results, using it's member function aStar()
    //which executes the A* Search algorithm on an initial and goal node
    Puzzle_Tree* tree;
    //three 3x3 arrays to hold the two initial state to choose from, and the goal state
    int initState1[3][3];
    int initState2[3][3];
    int initState3[3][3];
    int goalState[3][3];
    //flag variable to indicate whether the program should run again
    char restart = 'y';
    //values that hold the user's choice of initial state and heuristic function to use
    int stateID, heurID;
    //create a variable to read in input files data
    ifstream inFile;
    //open the file holding the two initial states
    inFile.open("data/initialStates.txt");
    //check for failure to open the file, if so print error message and terminate program
    //NOTE: Third initial state added to accomodate for required 6 runs of the program required in the report
    if(!inFile){
        cout<<endl
            <<"*PROGRAM TERMINATED*"<<endl
            <<"inFile (initialStates.txt) failed to open"<< endl;
            return 1;
    }
    else{
        //read in initial state 1
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                while(!(inFile >> initState1[i][j])){
                    cout << "Error reading number " + to_string(i) + "x" + to_string(j) + " in initial state 1.";
                    return 1;
                }
            }
        }
        //read in initial state 2
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                while(!(inFile >> initState2[i][j])){
                    cout << "Error reading number " + to_string(i) + "x" + to_string(j) + "in initial state 2.";
                    return 1;
                }
            }
        }
        //read in initial state 3 
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                while(!(inFile >> initState3[i][j])){
                    cout << "Error reading number " + to_string(i) + "x" + to_string(j) + "in initial state 2.";
                    return 1;
                }
            }
        }
    }
    //close initial state input file
    inFile.close();

    //open the file holding the goal state
    inFile.open("data/goalState.txt");
    //check for failure to open the file, if so print error message and terminate program
    if(!inFile){
        cout<<endl
            <<"*PROGRAM TERMINATED*"<<endl
            <<"inFile (goalState.txt) failed to open"<< endl;
            return 1;
    }
    else{
        //read in goal state
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                while(!(inFile >> goalState[i][j])){
                    cout << "Error reading number " + to_string(i) + "x" + to_string(j) + "in goal state.";
                    return 1;
                }
            }
        }
    }
    //close goal state input file
    inFile.close();

    //repeat main program for as long as user wants
    while(restart != 'n'){
        //clear screen of metrics from previous run
        system("cls");
        //print the two initial states for the user to view and choose from
        cout << "Initial State #1" << endl;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                cout << initState1[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl << "Initial State #2" << endl;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                cout << initState2[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl << "Initial State #3" << endl;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                cout << initState3[i][j] << " ";
            }
            cout << endl;
        }
        //repeatedly ask for the user to choose initial state 1 or 2 until they enter '1', '2', or '3'
        do{
            cout << "Choose initial state '1', '2' or '3': ";
            cin >> stateID;
            cout << endl;
        }while(stateID != 1 && stateID != 2 && stateID != 3);

        //print the two heuristic's names and definitions for the user to view and choose from
        cout << "Heuristic 1: Manhattan Distance Heuristic" << endl
             << "\tCalculates how far off a state is from the goal state by summing the horizontal and vertical distances" << endl
             << "\teach number must travel to reach it's final position."<< endl << endl;
        cout << "Heuristic 2: Entanglement Heuristic (My Custom Heuristic)" << endl
             << "\tCalculates how far off a state is from the goal state by summing the number of groups of adjacent numbers" << endl
             << "\tthat are in the incorrect order relative to each other." << endl << endl;
        //repeatedly ask for the user to choose heuristic 1 or 2 until they enter '1' or '2'
        do{
            cout << "Choose heuristic '1' or '2': ";
            cin >> heurID;
            cout << endl;
        }while(heurID != 1 && heurID != 2);

        //clear screen
        system("cls");
        
        //if initial state 1 was chosen
        if(stateID == 1){
            //if heuristic 1 was chosen
            if(heurID == 1){
                //create a new Puzzle_Tree object with initial state 1, and heurisitic 1
                tree = new Puzzle_Tree(initState1, goalState, stateID, heurID);
                //run the A* Search algorithm on the tree
                tree->aStar();
            }
            //if heurisitc 2 was chosen
            else{
                //create a new Puzzle_Tree object with initial state 1, and heuristic 2
                tree = new Puzzle_Tree(initState1, goalState, stateID, heurID);
                //run the A* Search algorithm on the tree
                tree->aStar();
            }
        }
        //else if initial state 2 was chosen
        else if(stateID == 2){
            //if heuristic 1 was chosen
            if(heurID == 1){
                //create a new Puzzle_Tree object with initial state 2, and heuristic 1
                tree = new Puzzle_Tree(initState2, goalState, stateID, heurID);
                //run the A* Search algorithm on the tree
                tree->aStar();
            }
            //if heuristic 2 was chosen
            else{
                //create a new Puzzle_Tree object with initial state 2, and heuristic 2
                tree = new Puzzle_Tree(initState2, goalState, stateID, heurID);
                //run the A* Search algorithm on the tree
                tree->aStar();
            }
        }
        //else if initial state 3 was chosen
        else{
            //if heuristic 1 was chosen
            if(heurID == 1){
                //create a new Puzzle_Tree object with initial state 3, and heuristic 1
                tree = new Puzzle_Tree(initState3, goalState, stateID, heurID);
                //run the A* Search algorithm on the tree
                tree->aStar();
            }
            //if heuristic 2 was chosen
            else{
                //create a new Puzzle_Tree object with initial state 3, and heuristic 2
                tree = new Puzzle_Tree(initState3, goalState, stateID, heurID);
                //run the A* Search algorithm on the tree
                tree->aStar();
            }

        }
        //delete the dynamically allocated tree
        delete tree;

        //repeatedly ask the user if they want to restart the program until they enter 'y' or 'n'
        do{
            cout << "Restart the program? (y/n)" << endl;
            cin >> restart;
        }while(restart != 'y' && restart != 'n');
    }
}