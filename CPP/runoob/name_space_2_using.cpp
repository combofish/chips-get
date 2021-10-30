#include <iostream>

using std::cout;
//using std::endl;

namespace namespace1{
  void func(){
    cout << "call func in namespace1" << std::endl;
  }
}

namespace namespace2{
  void func(){
    cout << "call func in namespace2" << std::endl;
  }
}

using namespace namespace2;

int main(){
  func();  

  return 0;
}
