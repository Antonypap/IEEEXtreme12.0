#include <iostream>
#include <vector>
#include <string>

using namespace std;

class PartitionCounter {
    // Return the number of subsequences of the suffix of v beginning at position k
    // that are (a) valid, given that the initial depth of the subsequence is d (on
    // account of it being the suffix of some larger subsequence), and (b)
    // leave behind a remainder subsequence that is also valid, given that
    // the remainder sequence has initial depth depths[k]-d.
    int count(int d, int k) {
        // If a prefix of either sequence (selected or remaining) has more ']'s
        // than '['s then there can't be any completing subsequences.
        if (d < 0 || depths[k] - d < 0) {
            return 0;
        }

        // Only compute the answer if we haven't already.
        if (memo[d][k] == -1) {
            // A subsequence must either contain no elements, or a leftmost element
            // at some position.  All subsequences produced by recursion after this
            // initial choice are distinct (when considering the sequence of
            // character indices included, though not necessarily when considering
            // the sequence of characters themselves).

            // Try including no elements.  This effectively terminates the larger
            // subsequence that the selected subsequence is part of, so it can be
            // legal only if its depth is 0.  It also effectively includes all
            // remaining characters in the remainder sequence, but if the selected
            // subsequence has depth 0 and the original string does too, then it's
            // implied that the remainder must also have total depth 0, so we don't
            // need to check it.
            int n = (d == 0);

            // Try including a leftmost element at each remaining position.
            // If this would cause a remainder subsequence that has negative
            // depth, stop: any later loop iterations would also create illegal
            // remainder subsequences.
            for (unsigned int i = k; i < v.size() && depths[i] - d >= 0; ++i) {
                n += count(d + v[i], i + 1);
            }

            memo[d][k] = n;
        }

        return memo[d][k];
    }

    vector<int> v;          // 1 for '[', -1 for ']'
    vector<int> depths;     // depths[i] is the sum of the 1st i elements
    vector<vector<int> > memo;  // DP matrix.  -1 => not computed yet

public:
    PartitionCounter(string s) : memo(s.size() / 2 + 1, vector<int>(s.size() + 1, -1)) {
        depths.push_back(0);
        int total = 0;
        for (unsigned int i = 0; i < s.size(); ++i) {
            v.push_back(1 - 2 * (s[i] == ']')); // Map '[' to 1 and ']' to -1
            depths.push_back(total += v[i]);
        }
    }

    int count() {
        if (depths.back() == 0) {
            return count(0, 0);
        } else {
            return 0;       // Need to handle invalid strings specially
        }
    }
};

int main(int argc, char **argv) {
  string a;
  cin >> a;
  PartitionCounter c(a);
  cout << c.count() << '\n';
}
