#include <iostream>
// #include <string>
using namespace std;

string vernam_cipher(string p, string key){
    string k1 = key;
    while(k1.length() < p.length()){
        k1 += key;
    }
    string cipher = "";
    for(int i = 0; i < p.length(); i++){
        cipher += ((p[i] - 'a' + 1) ^ (k1[i] - 'a' + 1)) % 26 + 'a' - 1;
    }
    return cipher;
}

int main(){
    string p, key;
    cout << "Enter plain text : ";
    cin >> p;
    cout << "Enter key : ";
    cin >> key;
    string cipher_txt = vernam_cipher(p, key);
    cout << "cipher text : " << cipher_txt;
    return 0;
}
