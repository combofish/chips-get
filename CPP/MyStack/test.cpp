#include "custom_template_stack.h"
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

void printStack(CStack<string> &sta) {
  cout << "Print stack: ";
  for (int i = 0; i < sta.size(); i++) {
    cout << sta[i] << " ";
  }
  cout << endl;
}

int main() {
  CStack<string> sta(3);

  std::stringstream ss1("hello"), ss2("world");

  ss1 >> sta;
  ss2 >> sta;

  printStack(sta);
  cout << sta << endl;
  printStack(sta);
  return 0;
}
