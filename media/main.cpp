#include <iostream>
#include "DynamicDequeue.cpp"

using namespace std;

int main(){
    DynamicDequeue q;
    double a = 0;
    long int num_of_elements = 1000*500;
    for(int i =0 ;i<num_of_elements;i++){
        q.insertFront(a);
    }
}