#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

void knapsack(const int&, const int&, const vector<int>&, const vector<int>&);

int weights[50], values[50];
int C[50][50];

int main(){
	int n, W;

	cout << "Enter number of items:" << endl;;
	cin >> n;
	cout << "Enter Capacity" << endl;
	cin >> W;
	cout << "Enter weights" << endl;

	vector<int> weights(n), values(n);
	

	for(int i = 0; i < n; i++){
		cin >> weights[i];
	}

	cout << "Enter values" << endl;

	for(int i = 0; i < n; i++){
		cin >> values[i];
	}

	knapsack(n, W, weights, values);

	system("pause");
}

void knapsack(const int& n, const int& W, const vector<int>& weights, const vector<int>& values){

	int C[n][n];

	for(int i = 1; i <= n; i++){
		C[i][0] = 0;
	}
	for(int i = 1; i <= n ; i++){
		for(int w = 0; w <= W; w++){
			if(weights[i] <= w){
				if(values[i] + C[i-1][w - weights[i]] > C[i-1][w])
					C[i][w] = values[i] + C[i-1][w - weights[i]];
				else
					C[i][w] = C[i-1][w];
			}
			else
				C[i][w] = C[i-1][w];
		}
	}
}
