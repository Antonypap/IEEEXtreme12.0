
// C++ program to find Minimum number
// of  changes to make array distinct
#include <bits/stdc++.h>
using namespace std;

// Fucntion that returns minimum number of changes
int minimumOperations(std::vector<int> a, int n)
{

    // Hash-table to store frequency
    unordered_map<int, int> mp;

    // Increase the frequency of elements
    for (int i = 0; i < n; i++)
        mp[a[i]] += 1;

    int count = 0;

    // Traverse in the map to sum up the (occurences-1)
    // of duplicate elements
    for (auto it = mp.begin(); it != mp.end(); it++) {
        if ((*it).second > 1)
            count += (*it).second-1;
    }
    return count;
}

// Driver Code
int main()
{
    int N;
    std::cin >> N;
    std::vector<int> dest;
    for(int i = 0; i < N; i++)
    {
        int a;
        std::cin >> a;
        dest.push_back(a);
    }

    cout << minimumOperations(dest, N);
    return 0;
} 
