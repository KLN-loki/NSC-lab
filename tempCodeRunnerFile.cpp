#include <bits/stdc++.h>
using namespace std;

string encryption(string str, int key);
string decryption(string ct, int key);

int main(){
    string str;
    cout << "Enter plain text : ";
    getline(cin, str);
    int key;
    cout << "Enter key : ";
    cin >> key;
    string ct = encryption(str, key);
    cout << "Cipher text after encryption : " << ct << endl;
    string dt = decryption(ct, key);
    cout << "Plain text after decryption : " << dt << endl;
    return 0;
}

string encryption(string str, int key){
    string ct = "";
    for (int i = 0; i < str.length(); i++){
        if(str[i] == ' '){
            ct.push_back(str[i]);
        }
        else{
            ct.push_back((str[i] + key - 'a') % 26 + 'A');
        }
    }
    return ct;
}

string decryption(string ct, int key){
    string dt = "";
    for (int i = 0; i < ct.length(); i++){
        if(ct[i] == ' '){
            dt.push_back(ct[i]);
        }
        else{
            dt.push_back((ct[i] - key - 'A') % 26 + 'a');
        }
    }
    return dt;
}