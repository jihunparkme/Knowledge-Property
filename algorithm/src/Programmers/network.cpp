#include <string>
#include <vector>
#include <iostream>

using namespace std;

void dfs(int s, vector<vector<int>> &computers, vector<int> &visited, int n) {
	visited[s] = 1;
	for (int i=0; i < n; i++) {
		if (!visited[i] && computers[s][i] == 1) {
			dfs(i, computers, visited, n);
		}
	}
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	vector<int> visited(n);

	for (int i = 0; i < n; i++) {
		if (!visited[i]) {
			dfs(i, computers, visited, n);
					answer++;
		}
	}
	return answer;
}

int main(void)
{
	int n = 3;
	vector<vector<int>> computers = { { 1, 1, 0 },{ 1, 1, 0 },{ 0, 0, 1 } };
	cout << solution(3, computers) << '\n';
}