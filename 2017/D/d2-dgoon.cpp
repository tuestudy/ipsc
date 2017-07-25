#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>

using namespace std;

int T = 0;
set<int> nbs;

void solve() {
  int n = 0;
  cin >> n;
  if (nbs.find(n) != nbs.end()) {
    printf("1 %d\n", n);
    return;
  }

  for (const int& i : nbs) {
    if (i >= n) break;
    int r = n - i;
    if (nbs.find(r) != nbs.end()) {
      printf("2 %d %d\n", r, i);
      return;
    }
  }
}

void loadNonBorings() {
  ifstream infile("nonborings.txt");
  while (infile) {
    int n;
    infile >> n;
    nbs.insert(n);
  }
  //printf("Load all nonborings\n");
}

int main() {
  loadNonBorings();
  cin >> T;
  for(int i = 0; i < T; ++i) {
    solve();
  }
  return 0;
}
