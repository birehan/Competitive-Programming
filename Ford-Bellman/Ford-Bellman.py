#include <iostream>
#include <vector>
#include <tuple>
#include <limits>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> costs(n, numeric_limits<int>::max());
    vector<tuple<int, int, int>> edges;

    for (int i = 0; i < m; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        edges.push_back(make_tuple(a - 1, b - 1, cost));
    }

    int startNode = 0;  // Start node (0-based index)

    costs[startNode] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : edges) {
            int a = get<0>(edge);
            int b = get<1>(edge);
            int cost = get<2>(edge);
            if (costs[a] != numeric_limits<int>::max() && costs[a] + cost < costs[b]) {
                costs[b] = costs[a] + cost;
            }
        }
    }

    // Check for negative cycles
    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : edges) {
            int a = get<0>(edge);
            int b = get<1>(edge);
            int cost = get<2>(edge);
            if (costs[a] != numeric_limits<int>::max() && costs[a] + cost < costs[b]) {
                cout << "Negative cycle detected!" << endl;
                return 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (costs[i] != numeric_limits<int>::max()) {
            cout << costs[i] << " ";
        } else {
            cout << 30000 << " ";
        }
    }

    cout << endl;

    return 0;
}
