#include <iostream>

using namespace std;

namespace namespace1 {
  void func(){
    cout << "call namespace1 func" << endl;
  }

}

namespace namespace2{
  void func(){
    cout << "call namespace2 func" << endl;
  }
  
}

int main(){
  namespace2::func();
  namespace1::func();  
    
  return 0;
}
