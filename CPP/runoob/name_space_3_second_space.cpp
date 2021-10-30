#include <iostream>

using namespace std;

namespace firstnamespace{
  void func(){
    cout << "in firstnamespace func" << endl;
  }

  namespace secondnamespace{
    void func(){
      cout << "in secondnamespace func" << endl;
    }
  }
}

using namespace firstnamespace::secondnamespace;
int main(){
  func();

  return 0;
}
