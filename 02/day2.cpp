#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
  char panel1[3][3] = 
  {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'}
  };

  int x1 = 1;
  int y1 = 1;

  char panel2[5][5] =
  {
    {' ', ' ', '1', ' ', ' '},
    {' ', '2', '3', '4', ' '},
    {'5', '6', '7', '8', '9'},
    {' ', 'A', 'B', 'C', ' '},
    {' ', ' ', 'D', ' ', ' '}
  };

  int x2 = 0;
  int y2 = 2;

  string data;
  cout << "day1 | day2" << endl;
  while (cin >> data) {
    for (char c : data) {
      if (c == 'D' && y1 < 2) y1++;
      if (c == 'U' && y1 > 0) y1--;
      if (c == 'R' && x1 < 2) x1++;
      if (c == 'L' && x1 > 0) x1--;

      if (c == 'D' && y2 < 4 && panel2[y2+1][x2] != ' ') y2++;
      if (c == 'U' && y2 > 0 && panel2[y2-1][x2] != ' ') y2--;
      if (c == 'R' && x2 < 4 && panel2[y2][x2+1] != ' ') x2++;
      if (c == 'L' && x2 > 0 && panel2[y2][x2-1] != ' ') x2--;
    }

    cout << "  " << panel1[y1][x1] << "  |  " << panel2[y2][x2] << endl;
  }
}
