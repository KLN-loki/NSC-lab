#include <bits/stdc++.h>
using namespace std;

int main(){
    // vector <pair<int, int>> ch;
    for (int i = 0; i < 128; i = i+4){
        char ch1 = i, ch2 = i + 1, ch3 = i + 2, ch4 = i + 3;
        cout << i << "  " << ch1 << " | " <<  i + 1 << "  " << ch2 << " | " << i + 2 << "  " << ch3 << " | " << i + 3 << "  " << ch4 << " | " <<  endl; 
    }
    return 0;
}