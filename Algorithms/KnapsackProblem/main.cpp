#include <iostream>

using namespace std;

int main(){
    //input values
    int n, w;
    int profits[n];
    int weights[n];

    
    //read input 
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> profits[i]; 
    }
    for(int i = 0; i < n; i++){
        cin >> weights[i];
    }
    cin >> w;

    int arr[n+1][n+1];

    for(int i = 0; i < n; i++){                                                                 //iterate through items available
        for(int j = 0; j < w; j++){                                                             //iterate through weight available
            if ( i == 0 || w == 0){                                                             //if there are 0 items or 0 weight available 
                arr[i][j] = 0;                                                                  //set the max profits of i items and w weight = 0
            }
            else if(weights[i-1] <= j){                                                          //if previous items' weight is less than or equal to the available weight
                arr[i][j] = max(profits[i-1] + arr[i-1][w - weights[i-1]], arr[i-1][j]);       //set the max profits of i items and w weight to the max value between
            }                                                                                   
            else{                                                                               //else
                arr[i][j] = arr[i-1][j];                                                        //set the max profits of the i items and w weights to the previous one
            }
        }
    }
    cout << arr[n][w];                                                                          //print out the max profits 

    return 0;
}