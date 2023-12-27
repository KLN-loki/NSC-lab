#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

const int mod = 26;

vector<vector<int>> constructMatrix(const string &text, const string &key, int keyMatrixDim) {
    vector<vector<int>> keyMatrix(keyMatrixDim, vector<int>(keyMatrixDim, 0));
    for (int i = 0; i < key.length(); ++i) {
        keyMatrix[i / keyMatrixDim][i % keyMatrixDim] = key[i] - 'A';
    }

    vector<vector<int>> textMatrix;
    for (int i = 0; i < text.length(); i += keyMatrixDim) {
        vector<int> row;
        for (int j = 0; j < keyMatrixDim; ++j) {
            row.push_back(text[i + j] - 'A');
        }
        textMatrix.push_back(row);
    }

    return textMatrix;  // Returning only text matrix for simplicity
}

vector<int> matrixMultiplication(const vector<vector<int>> &keyMatrix, const vector<int> &plainTextRow) {
    vector<int> result(keyMatrix.size(), 0);
    for (int i = 0; i < keyMatrix.size(); ++i) {
        for (int j = 0; j < keyMatrix[0].size(); ++j) {
            result[i] += keyMatrix[i][j] * plainTextRow[j];
        }
        result[i] %= mod;
    }
    return result;
}

vector<int> encryption(const string &plainText, const string &key) {
    int keyLength = key.length();
    int textLength = plainText.length();
    int keyMatrixDim = sqrt(keyLength);

    auto textMatrix = constructMatrix(plainText, key, keyMatrixDim);

    vector<int> cipher;
    for (int i = 0; i < textLength / keyMatrixDim; ++i) {
        auto row = matrixMultiplication(textMatrix, textMatrix[i]);
        for (auto &num : row) {
            cipher.push_back(num + 'A');
        }
    }
    return cipher;
}

vector<int> matrixVectorMod(const vector<vector<int>> &keyMatrix, const vector<int> &cipherRow, int modInv) {
    vector<int> result(keyMatrix.size(), 0);
    for (int i = 0; i < keyMatrix.size(); ++i) {
        for (int j = 0; j < keyMatrix[0].size(); ++j) {
            result[i] += keyMatrix[i][j] * cipherRow[j];
        }
        result[i] *= modInv;
        result[i] %= mod;
        if (result[i] < 0) {
            result[i] += mod;
        }
    }
    return result;
}

vector<int> decryption(const vector<int> &cipher, const string &key, int textLength, int keyMatrixDim) {
    auto keyMatrix = constructMatrix(key, key, keyMatrixDim);  // Using key as text for simplicity
    auto keyMatrixInv = keyMatrix;  // Need to calculate the inverse of the key matrix

    vector<int> text;
    int modInv = 8;  // inverse of 2 modulo 26
    for (int i = 0; i < textLength / keyMatrixDim; ++i) {
        auto row = matrixVectorMod(keyMatrixInv, vector<int>(cipher.begin() + i * keyMatrixDim, cipher.begin() + (i + 1) * keyMatrixDim), modInv);
        for (auto &num : row) {
            text.push_back(num + 'A');
        }
    }
    return text;
}

int main() {
    string plainText, key;
    cout << "Enter the plain text: ";
    getline(cin, plainText);
    cout << "Enter the key: ";
    getline(cin, key);

    int keyLength = key.length();
    int textLength = plainText.length();
    int keyMatrixDim = sqrt(keyLength);

    auto cipherMatrix = encryption(plainText, key);

    cout << "Cipher text: ";
    for (auto num : cipherMatrix) {
        cout << static_cast<char>(num);
    }
    cout << endl;

    auto text = decryption(cipherMatrix, key, textLength, keyMatrixDim);

    cout << "Plaintext: ";
    for (auto num : text) {
        cout << static_cast<char>(num);
    }
    cout << endl;
    return 0;
}