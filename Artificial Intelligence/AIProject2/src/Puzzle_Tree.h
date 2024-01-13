#ifndef PUZZLE_TREE_H
#define PUZZLE_TREE_H

#include <vector>
#include <chrono>
#include <map>
#include <unordered_set>

class Puzzle_Tree{
    public:
        Puzzle_Tree(int [3][3], int [3][3], int, int);
        void aStar();
    
    private:
        //node struct to represent a state of the 8 Puzzle problem including is h, g, and f values, a pointer to it's parent and 
        //a vector of pointers to it's children. Includes a hashing function that uses the Cantor pairing function to create hashcodes
        //for a particular state, and a comparison function.
        struct node{
            int state[3][3];
            int fVal;
            int gVal;
            int hVal;
            vector<node*> children;
            node* parent;

        struct Hasher {
            size_t operator()(const node* n) const {
                size_t hash = 0;
                int k = 0;
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        hash += CantorPairing(k++, n->state[i][j]);
                    }
                }
                return hash;
            }

            // Cantor pairing function
            size_t CantorPairing(size_t x, size_t y) const {
                return (x + y) * (x + y + 1) / 2 + y;
            }
        };

        struct EqualFn {
            bool operator()(const node* n1, const node* n2) const {
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        if (n1->state[i][j] != n2->state[i][j]) {
                            return false;
                        }
                    }
                }
                return true;
            }
        };
    };
        //node holding initial state.
        node initNode;
        //node holding goal state
        node goalNode;
        //map that maps the numbers of the goal state in a left to right, top to bottom fashion to numbers 0 to 8
        map<int, int> goalMap;
        //holds the ID of the state being used
        int stateID;
        //holds the ID of the heuristic being used
        int heurID;
        //keeps track of the depth of the tree
        int depth;
        //keeps track of the total number of nodes generated
        int nodesGen;
        //keeps track of the total number of nodes expanded
        int nodesExp;
        //Hash table of nodes that have yet to be expanded
        unordered_set<node*, node::Hasher, node::EqualFn> open;
        //Hash table of nodes that have been expanded
        unordered_set<node*, node::Hasher, node::EqualFn> closed;
        //Holds the start time of the A* Search algorithm
        std::chrono::time_point<std::chrono::system_clock> startTime;
        //Holds the sto ptime of the A* Search algorithm
        std::chrono::time_point<std::chrono::system_clock> stopTime;
        
        bool isAncestor(node*);
        void printMetrics();
        void propogate(node*);
        void manhattanHeur(node*);
        void entanglementHeur(node*);
        bool inOrder(vector<int>, vector<int>);
        void mergeGroups(vector<vector<int>>&, int);
        void deallocate(node*);
        void setDepth(int);
        void printTP();
        void genChildren(node*);
};
#endif