#include <iostream>
#include <utility>


class Test{};

template <typename T>
void func(T&& t){
    cout<< "call func"<<endl;
}

int main(){
    Test a;
    func(a);
    funct(move(a));

    return 0;
}