// C++ program for weighted job scheduling using Dynamic Programming.
#include <iostream>
#include <algorithm>
#include <vector>

// A utility function that is used for sorting events
// according to finish time
bool jobComparataor(Star* s1, Star* s2)
{
    return (s1->m_finishTime < s2->finishTime);
}

// Find the latest job (in sorted starsay) that doesn't
// conflict with the job[i]
int latestNonConflict(std::vector<Star*> stars, int i)
{
    for (int j = i - 1; j >= 0; j--)
    {
        if (stars[j]->m_finishTime <= stars[i]->m_startTime)
            return j;
    }
    return -1;
}

// The main function that returns the maximum possible
// profit from given starsay of jobs
int findMaxProfit(std::vector<Star*> stars)
{
    // Sort jobs according to finish time
    sort(stars.begin(), stars.end(), jobComparataor);

    // Create an starsay to store solutions of subproblems.  table[i]
    // stores the profit for jobs till stars[i] (including stars[i])
    std::vector<int> table(stars.size());
    table.push_back(stars[0]->m_desirability);

    // Fill entries in M[] using recursive property
    for (unsigned int i = 1; i < stars.size(); i++)
    {
        // Find profit including the current job
        int desire = stars[i]->m_desirability;
        int l = latestNonConflict(stars, i);
        if (l != -1)
            desire += table[l];

        // Store maximum of including and excluding
        table[i] = max(desire, table[i-1]);
    }

    int result = table[stars.size()-1];
    return result;
}

class Star
{
public:
  int m_startTime, m_finishTime, m_desirability;

  Start(int startTime, int finishTime, int desirability) : m_startTime(startTime), m_finishTime(finishTime), m_desirability(desirability) {}
}

bool isOverlapping(std::vector<Star*> stars, Star* star)
{
  for(auto it : stars)
  {
    if(star->m_startTime < it->m_finishTime || star->m_finishTime > it->m_startTime)
    {
      return true;
    }
  }
  return false;
}
// Driver program
int main()
{
    int N;
    std::cin >> N;
    std::vector<Star*> stars;
    for(int i = 0; i < N; i++)
    {
      int startTime, finishTime, desirability;
      std::cin >> startTime >> finishTime >> desirability;
      Star* star = new Star(startTime, finishTime, desirability);

    }

    cout << "The optimal profit is " << findMaxProfit(stars);
    return 0;
}
