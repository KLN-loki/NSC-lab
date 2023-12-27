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
    for (int i = 0; i < ct.length(); i++){
        if (ct[i] >= 'a' && ct[i] <= 'z'){
            char x = toupper(ct[i]); 
            cout << x;
        }
        else cout << ct[i];
    }
    cout << endl;
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
            if(str[i] >= 'a' && str[i] <= 'z'){
                ct.push_back((str[i] + key - 'a') % 26 + 'a');
            }
            else if(str[i] >= 'A' && str[i] <= 'Z'){
                ct.push_back((str[i] + key - 'A') % 26 + 'A');
            }
            else if(str[i] >= '0' && str[i] <= '9'){
                ct.push_back((str[i] + key - '0') % 10 + '0');
            }
            else {
                ct.push_back((str[i] + key) % 127);
            }
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
            if(ct[i] >= 'a' && ct[i] <= 'z'){
                dt.push_back((ct[i] - key - 'a') % 26 + 'a');
            }
            else if(ct[i] >= 'A' && ct[i] <= 'Z'){
                dt.push_back((ct[i] - key - 'A') % 26 + 'A');
            }
            else if(ct[i] >= '0' && ct[i] <= '9'){
                dt.push_back((ct[i] - key - '0') % 10 + '0');
            }
            else {
                dt.push_back((ct[i] - key) % 127);
            }
        }
    }
    return dt;
}