using namespace std;

#include "Puzzle_Tree.h"
#include <vector>
#include <chrono>
#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <stack>
#include <cstdlib>
#include <map>
#include <cstring>

//Class constructor: Sets the state of the initial and goal nodes to the 2D arrays init and goal, respectively. 
//Sets the gVal of the inital node to 0 and sets it's parent to NULL. 
//Sets the numbers that record which initial state and heuristic is being used.
//Maps the integer elements of the goal 2D array to numbers 1 - 9
Puzzle_Tree::Puzzle_Tree(int init[3][3], int goal[3][3], int state, int heur){
    //for each position [i][j] set initNode's state to match init, and goalNode's state to match goal
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            initNode.state[i][j] = init[i][j];
            goalNode.state[i][j] = goal[i][j];
        }
    }
    //set initNode's gVal value and parent pointer
    initNode.gVal = 0;
    initNode.parent = NULL;
    //Sets the stateId and heurID to the user's choice
    stateID = state;
    heurID = heur;
    //set nodesGen, nodesExp, and depth to 0
    nodesGen = 0;
    nodesExp = 0;
    depth = 0;
    //map goal's elements to numbers 1 - 9, going left to right, top to bottom.
    int idx = 1;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            goalMap[goal[i][j]] = idx;
            idx++;
        }
    }
}

//The A* Final Function: Searches for a node with a state matching the goalNode's state. It does this by selecting and removing the
//node(best) with the lowest fVal value in open. If best matches the goal, it calls functions printMetrics() and deallocate() and then
//returns to main. Otherwise, it calls genChildren() and iterates through all of best's children nodes(child). If child's state 
//matches another node's(old) state in open, it saves child's gVal then replaces child with the old as a child of best. If the saved 
//gVal is less than old's gVal, the program sets old's gVal to child's gVal, it reset's old's parent to best, and it generate's old's 
//new fVal based on the new gVal. If child is not in open but is in closed, the child and old not go through the same process as if
//it were found in open, but it also propogates the changes made to old to old's children. If child is neither in open or closed the
//child is added to open. This process is repeated until node matching goalNode's state is found or until open is empty. This function
//also keeps track of some of the metrics(execution time, nodes generated, nodes expanded) that are later reported.
void Puzzle_Tree::aStar(){
    //Get the start time for the execution time metric
    startTime = std::chrono::system_clock::now();
    //create a node pointer to point to the node in open with the lowest fVal
    node* bestNode;
    //Add initNode to open
    open.insert(&initNode);
    //while open is not empty
    while(!open.empty()){
        //create an integer that holds the max possible integer value, to compare to the fVal values, and later hold a fVal lower than it
        int lowestF = numeric_limits<int>::max();
        //for every node pointer(n) in open
        for(node* n : open){
            //if n's fVal is less than the current value of lowestF
            if(n->fVal < lowestF){
                //set lowestF to this lower fVal
                lowestF = n->fVal;
                //set bestNode to point to the node n is pointing to.
                bestNode = n;
            }
        }
        //remove bestNode from open
        open.erase(bestNode);
        //add bestNode to closed                    
        closed.insert(bestNode);
        //if bestNode's state and goalNode's state match. memcmp() compares two blocks of memory, it returns the difference in value
        //between the first two bytes to be different. If memcmp() returns 0 then the two blocks of memory match.
        if(memcmp(bestNode->state, goalNode.state, sizeof(bestNode->state)) == 0){
            //get the stop time for the execution time metric
            stopTime =  std::chrono::system_clock::now();
            //set the parent of goalNode to the parent of bestNode, this is important later for printing the total path from the 
            //initial node to the goal node
            goalNode.parent = bestNode->parent;
            //call printMetrics()
            printMetrics();
            //call deallocate()
            deallocate(&initNode);
            //exit
            return;
        }
        //else, call genChildren() on bestNode
        genChildren(bestNode);
        //bestNode has now been expanded and the nodesExp can be incremented for the nodes expaneded metric
        nodesExp += 1;
        //add the number of children of bestNode to the nodesGen for the nodes generated metric 
        nodesGen += bestNode->children.size();
        //for each childNode in bestNode's children
        for( node* childNode : bestNode->children){
            //search for childNode in open. find() returns an iterator to the element being searched for or to a point past 
            //the last element in open. Also, we do not have to provide childNode's state to find a node with a matching state.
            //open is a hashtable of node pointers, and it calculates a node pointer's hash code based on it's state.
            //So open.find(childNode) calculates childNode's hash code, and searches for a matching hashcode.
            auto it = open.find(childNode);
            //if a node matching childNode is in open
            if(it != open.end()){
                //save childNode's gVal value for future use
                int newG = childNode->gVal;
                //delete the redundant node childNode points to
                delete childNode;
                //set childNode to point to the node already in open
                childNode = *it;
                //if the path to the recently deleted node was shorter than the path to the new childNode
                if( newG < childNode->gVal){
                    //set childNode's gVal to newG
                    childNode->gVal = newG;
                    //reset childNode's parent to bestNode
                    childNode->parent = bestNode;
                    //reset childNode's fVal based on the change in gVal
                    childNode->fVal = childNode->gVal + childNode->hVal;
                }
            }
            //else if a node matching childNode is not in open
            else{
                //search for the childNode in closed
                auto it = closed.find(childNode);
                //if a node matching childNode is in closed
                if(it != closed.end()){
                    if(!isAncestor(childNode)){
                        //save childNode's gVal value for future use
                        int newG = childNode->gVal;
                        //delete the redundant node childNode points to
                        delete childNode;
                        //set childNode to point to the node already in closed
                        childNode = *it;
                        //if the path to the recently deleted node was shorter than the path to the new childNode
                        if( newG < childNode->gVal){
                            //set childNode's gVal to newG
                            childNode->gVal = newG;
                            //reset childNode's parent to bestNode
                            childNode->parent = bestNode;
                            //reset childNode's fVal based on the change in gVal
                            childNode->fVal = childNode->gVal + childNode->hVal;
                            //update all of childNode's children
                            propogate(childNode);
                        }
                    }
                }
                //else if a node matching childNode is not in open or closed
                else{
                    //add childNode to open
                    open.insert(childNode);
                }
            }
        }
    }
    //open is empty
    //report a failure
    cout << "Goal state could not be reached from initial state." << endl << endl;
    //call deallocate()
    deallocate(&initNode);
    //exit
    return;
}

//Determines if a node's state matches one of it's ancestor's states. If there is a match it returns true, if not it returns false
bool Puzzle_Tree::isAncestor(node* childNode) {
//create a node pointer that points to childNode's parent
node* ancestor = childNode->parent;
    //while the root node has not been reached
    while (ancestor != NULL) {
        //bool to indicate if childNode's state matches ancestor's state
        bool isSame = true;
        //for every position in the board
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                //if the numbers at position [i][j] in ancestor's state and childNode's state do not match
                if (ancestor->state[i][j] != childNode->state[i][j]) {
                    //set isSame to false
                    isSame = false;
                    break;
                }
            }
            if(!isSame) break;
        }
        //if isSame is true return true
        if(isSame) {
            return true;
        }
        //else set ancestor to ancestor's parent
        ancestor = ancestor->parent;
    }
    //return false
    return false;
}

//Prints the the initial state and heuristic used to search this tree. Also, prints the metrics of the complete and successful search. 
//Metrics incldue:
//Execution Time: The time it took to get from the start of the search to the end of it.
//Nodes Generated: The total number of nodes created in the search process.
//Nodes Expanded: The total number of nodes whom had generated children.
//Tree Depth: The longest path from the root to a leaf node in the tree.
//Branching Factor: The average number of children to a node
//Total Path: The series of states from the initial node/state to the node matching the goal node/state. Represents the steps that need
//            to be taken to reach the goal state from the inital state. 
void Puzzle_Tree::printMetrics(){
    //print the inital state number and the heuristic used for the search of this tree.
    cout << "Initial State #" << stateID << endl << endl;
    if(heurID == 1){
        cout << "Heuristic used: Manhattan Distance heurisitc" << endl; 
    }
    else{
        cout << "Heuristic used: Custom heuristic" << endl;
    }
    cout << "-------------------------------------------------------------------" << endl;
    //get the number of seconds between startTime and stopTime as a duration object, use .count() to extract the duration value
    std::chrono::duration<double> elapsed_seconds = stopTime - startTime;
    int bFactor;
    if(nodesGen == 0){
        bFactor = 0;
    }
    else{
        bFactor = nodesGen/depth;
    }
    //print the metrics, and call printTP() to print the total path
    cout << "Execution Time: " << elapsed_seconds.count() << " seconds" << endl
         << "Nodes Generated: " << nodesGen << endl
         << "Nodes Expanded: " << nodesExp << endl
         << "Tree Depth: " << depth + 1 << endl
         << "Effective Branching Factor: " << bFactor << endl
         << "Total Path: " << endl;
    printTP();
}

//Updates the gVal and fVal of the child nodes of a parent node whose gVal has also changed. The function does not update child nodes
//with fVal values that are better than the potential new fVal. 
void Puzzle_Tree::propogate(node* parent){
    //for every child node of the parent node
    for(node* child : parent->children){
        //calculate the potential new gVal as the parent's gVal + 1
        int newG = parent->gVal + 1;
        //A node's state never changes, so neither does it's hVal
        //calculate the potential new fVal as the new gVal + the child's hVal.
        int newF = newG + child->hVal;
        //if the newly calculated fVal is less than the child node's current fVal
        if(newF < child->fVal){
            //update the child node's gVal with newG
            child->gVal = newG;
            //call setDepth()
            setDepth(newG);
            //update the child node's fVal with newF
            child->fVal = newF;
            //since the child was updated, it's children (if any) must be updated as well
            propogate(child);
        } 
    }
}

//Manhattan Distance heuristic function. Calculates the hVal as the sum of all of the horizontal and vertical distances that each
//element in the node's state must move in order to get to it's correct and final position in goalNode's state.
void Puzzle_Tree::manhattanHeur(node* node){
    //set node's initial hVal to 0
    node->hVal = 0;
    //for a every position on a state
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            //if the element at position [i][j] on the node's state does not match the element at the same position on the 
            //goalNode's state 
            if(node->state[i][j] != goalNode.state[i][j]){
                //for every position in goalNode's state
                for(int k = 0; k < 3; k++){
                    for(int l = 0; l < 3; l++){
                        //if the element at position [k][l] on goalNode's state matches the element at posistion [i][j]  on the 
                        //node's state
                        if(goalNode.state[k][l] == node->state[i][j]){
                            //Add the vertical and horizontal distance from [i][j] to [k][l] to node's hVal
                            node->hVal = node->hVal + std::abs(k - i) + std::abs(l - j);
                        }
                    }
                }
            }
        }
    }
}

//Entanglement heuristic (My custom heuristic):
//My function counts the number of groupings of numbers that are out of order compared to the goal state, thus capturing 
//the degree to which the tiles are "entangled" with each other. 
//Some rules: 
//      A single number is an in order group.
//      A group may consists of a max of two subgroups, each of which may be made up of further subgroups
//      The correct order is read as top to bottom, and left to right.
//      Only the order of adjacent groups are considered, you cannot group two groups that are separated by another group.
//      The array undergoes rounds of groupings, it does not continue to grow one group until it reaches another group it is in order with.
//
//                                                              EXAMPLE 
//We have a goal state:  1 2 3                      and an inital state: 8 2 3
//                       8 0 4                                           1 4 6
//                       7 6 5                                           7 5 0
//The correct order is: 1 2 3 8 0 4 7 6 5           The initial order is: 8 2 3 1 4 6 7 5 0
//The inital state's h value is 7 because:
//Out of order groups:     |Why it is out of order:                        |The resulting groupings:          |Total out of order groups:
//(8, 2)                   |8 should come after 2                          |(8 2) 3 1 4 6 7 5 0               |           1
//(3, 1)                   |3 should come after 1                          |(8 2) (3 1) 4 6 7 5 0             |           2                
//NOTE: the group containing 4 is not grouped, at this point, because it is inorder with the group containing 6
//(6, 7)                   |6 should come after 7                          |(8 2) (3 1) 4 (6 7) 5 0           |           3
//(5, 0)                   |5 should come after 0                          |(8 2) (3 1) 4 (6 7) (5 0)         |           4
//NEXT ROUND OF GROUPINGS
//((8, 2), (3, 1))         |8 should come after 3, after 2, after 1        |((8 2) (3 1)) 4 (6 7) (5 0)       |           5
//NOTE: the group containing 4 is not grouped, at this point, because it is inorder with all the numbers in group (6 7)
//((6, 7), (5, 0))         |5 should come after 6, after 7, after 0        |((8 2) (3 1)) 4 ((6 7) (5 0))     |           6
//(4, ((6, 7), (5, 0)))    |5 should come after 6 after 7 after 4 after 0  |((8 2) (3 1)) (4 ((6 7) (5 0)))   |           7
//NOTE: the group containing 4 is now grouped, because it is out of order with the number 0 in the neighboring group.
//NEXT ROUND OF GROUPINGS
//No further groups can be made as all numbers in group ((8 2) (3 1)) come before the numbers in group (4 ((6 7) (5 0)))
//                                                          END OF EXAMPLE
//
//This function operates by unraveling the node's 2D state array into a 1D vector (unraveled), in a top to bottom, left to right manner.
//Then to make checking the order of groups simpler the goalMap is applied to unraveled. Now every element in unraveled is replaced
//with the index it should be located at to match with the goal state. A group (first) can be sorted and then the numbers in the next
//group (second) can easily determine if they are in order or not by checking that they are not less than the largest number in first. 
//The function repeats rounds of groupings until no more groups can be made, either because there is only 1 group left, or the 
//remaining groups are all in order with each other.  
void Puzzle_Tree::entanglementHeur(node* node){
    //create a vector to hold vectors(groups) of integers. Groups are not maintained as they are in the above example so that a group
    //of several numbers can be sorted. Instead, the number of groups are counted by incrementing node's hVal every time a new
    //group is formed
    vector<vector<int>> unraveled;
    //set node's initial hVal value to 0
    node->hVal = 0;
    //a boolean that indicates whether or not a new group was formed during a round of groupings.
    bool regrouped = true;
    //for every position [i][j] on the node's state
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            //push a new vector consisting of the mapped (using goalMap) element at position [i][j] on node's state to unraveled 
            unraveled.push_back(vector<int>{goalMap[node->state[i][j]]});
        }
    }

    //Until there is only 1 group, or all groups are in order with each other
    if(unraveled.size() != 1 || regrouped){
        //get the current size of unraveled
        int n = unraveled.size() - 1;
        //set regrouped to false, as no new groups have yet been made in this round
        regrouped = false;
        //from the first to the second to last group in unraveled
        for(int i = 0; i < n-1; i++){
            //if inOrder() returns that group i and group i+1 are not in order
            if(!inOrder(unraveled[i], unraveled[i+1])){
                //call mergeGroups()
                mergeGroups(unraveled, i);
                //set regrouped to true
                regrouped = true;
                //increment node's hVal
                node->hVal++;
            }
        }
    }
}

//engtanglementHeur() helper function. Returns true if all numbers in group i(vec1) and group i+1(vec2) are in order with each other.
//vec1 and vec2 are in order if every number in vec2 comes after the largest number in vec1.
bool Puzzle_Tree::inOrder(vector<int> vec1, vector<int> vec2){
    //get the size of vec1(n) and vec2(m)
    int n = vec1.size();
    int m = vec2.size();
    //if vec1 and vec2 are both only 1 number
    if(n == 1 && m == 1){
        //return that they are in order if vec2 comes after vec1
        if(vec1[0] < vec2[0]){
            return true;
        }
        //else return that they are out of order
        else{
            return false;
        }
    }
    //else if either vec1 or vec2 is more than one number.
    else{
        //for every number in vec2
        for(int i = 0; i < m; i++){
            //if vec2[i] comes before the largest number in vec1 return that they are out of order
            if(vec2[i] < vec1[n-1]){
                return false;
            }
        }
        //else return that they are in order
        return true;
    }
}

//entanglementHeur() helper function. Merges the numbers of group i and group i+1 in unraveled into a new sorted group. Replace
//group i with the new group, and remove group i+1 from unraveled. 
void Puzzle_Tree::mergeGroups(vector<vector<int>> &unraveled, int i){
    //a new vector to hold all the number of group i and group i+1 in unraveled
    vector<int> newVec;
    //get the size of group i(n) and group i+1(m)
    int n = unraveled[i].size();
    int m = unraveled[i+1].size();
    //add every number in group i to newVec
    for(int j = 0; j < n; j++){
        newVec.push_back(unraveled[i][j]);
    }
    //add every number in group i+1 to newVec
    for(int j = 0; j < m; j++){
        newVec.push_back(unraveled[i+1][j]);
    }
    //sort newVec in ascending order
    sort(newVec.begin(), newVec.end());
    //replace group i with newVec
    unraveled[i] = newVec;
    //remove group i+1 from unraveled
    unraveled.erase(unraveled.begin() + i + 1);
}

//Frees all dynamic data that was reserved during tree building. The function does a depth first traversal of the tree, deleting leaf
//nodes as they appear.
void Puzzle_Tree::deallocate(node* root) {
    if (root == nullptr) {
        return;
    }
    for (node* child : root->children) {
        deallocate(child);
    }
    delete root;
}

//Keeps track of the depth of the tree by comparing the current depth (the gVal of the node furthest from initNode), with the new gVal
//of a node.
void Puzzle_Tree::setDepth(int newDepth){
    //if the new depth is deeper than the current depth, set the current depth to the new depth
    if(depth < newDepth){
        depth = newDepth;
    }
}

//Prints each node's state on the direct path from the initial state to the goal state. The function starts at the goalNode pushing each
//node's state onto a stack, then moving to the node's parent. It then prints the initial state, because the root node's parent
//is NULL and thus will not be pushed onto the stack, followed by each state at the stack's top as they are removed.
void Puzzle_Tree::printTP(){
    //create a node to iterate from the goal node to the initial node and then back down to the goal node
    node* iter = &goalNode;
    //create a stack of node pointers to represent the path from the initial node to the goal node
    stack<node*> TPinOrder;
    //while the current node's parent is not NULL
    while(iter->parent != NULL){
        //add the node to TPinOrder
        TPinOrder.push(iter);
        //move up to the current node's parent
        iter = iter->parent;
    }
    //print the root node's state since it is not added to the stack
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << iter->state[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    //while the stack is not empty
    while(!TPinOrder.empty()){
        //set the pointer to the node at the stack's top
        iter = TPinOrder.top();
        //print the node's state
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                cout << iter->state[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
        //remove the current node from the stack
        TPinOrder.pop();
    } 
}

//Generates all the possible children of a node (parent) and initializes their variables. A new node (child) is created for every
//position adjacent to the position in parent's state that contains the integer 0. 
void Puzzle_Tree::genChildren(node* parent){
    //A vector that allows for ease of moving to adjacent positions. For a position [i][j] all adjacent positions can be reached by
    //adding directions[i] to i, and directions[i+1] to j. Using i = 0 selects the positon to the left of [i][j], i = 1 select the 
    //position above, i = 2 selects the position to the right, and i = 3 selects the position below.  
    vector<int> directions = {-1, 0, 1, 0 , -1};
    //x and y hold the position of 0 on the parent's state
    //a and b hold the adjacent position after directions[i] and directions[i+1] have been added to x and y.
    int x, y, a, b;
    //a pointer to new children.
    node* child;

    //for all positions on the parent's state
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            //if the element is 0
            if(parent->state[i][j] == 0){
                //set the x and y values to i and j respecively
                x = i;
                y = j;
                //set i and j to 3 to both loops are exited.
                i = 3;
                j = 3;
            }
        }
    }
    //for each pair of directions in directions
    for(int i = 0; i < 4; i++){
        //get the adjacent position[a][b] by adding directions[i] and directions[i+1] to x and y respectively
        a = x + directions[i]; 
        b = y + directions[i+1];
        //if both a and b are within the bounds of the board
        if((a >= 0 && a < 3) && (b >= 0 && b < 3)){
            //create a new node and set child to point to it
            child = new node;
            //copy parent's state to child's state
            copy(&parent->state[0][0], &parent->state[0][0] + 9, &child->state[0][0]);
            //set child's state position [x][y] to the number at positon [a][b] of the child's state
            child->state[x][y] = child->state[a][b];
            //set the number at child's state positon [a][b] to 0;
            child->state[a][b] = 0;
            //set child's gVal to parent's gVal + 1
            child->gVal = parent->gVal + 1;
            //call setDepth()
            setDepth(child->gVal);
            //set child's hVal with manhattanHeur() or entanglementHeur() based on heurID
            if(heurID == 1){
                manhattanHeur(child);
            }
            else{
                entanglementHeur(child);
            }
            //Calculate the child's fVal
            child->fVal = child->gVal + child->hVal;
            //set the chiild's parent to parent
            child->parent = parent;
            //add the child to parent's children
            parent->children.push_back(child);
        }
    }
}
