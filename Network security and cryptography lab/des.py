from itertools import permutations

class Simple_DES:
    def __init__(self):
        self.key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]  # extra example for checking purpose
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.key1 = [0] * 8
        self.key2 = [0] * 8

        self.IP = [2, 6, 3, 1, 4, 8, 5, 7]
        self.EP = [4, 1, 2, 3, 2, 3, 4, 1]
        self.P4 = [2, 4, 3, 1]
        self.IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

        self.S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
        self.S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    def key_generation(self):
        key_ = [self.key[self.P10[i] - 1] for i in range(10)]

        Ls = key_[:5]
        Rs = key_[5:]

        Ls_1 = self.shift(Ls, 1)
        Rs_1 = self.shift(Rs, 1)

        key1 = [Ls_1[i] for i in range(5)] + [Rs_1[i] for i in range(5)]
        self.key1 = [key1[self.P8[i] - 1] for i in range(8)]

        Ls_2 = self.shift(Ls, 2)
        Rs_2 = self.shift(Rs, 2)

        key2 = [Ls_2[i] for i in range(5)] + [Rs_2[i] for i in range(5)]
        self.key2 = [key2[self.P8[i] - 1] for i in range(8)]

        print("Your Key-1:")
        print(*self.key1)
        print("Your Key-2:")
        print(*self.key2)

    def shift(self, ar, n):
        return ar[n:] + ar[:n]

    def encryption(self, plaintext):
        arr = [plaintext[i] for i in range(8)]

        arr1 = self.function(arr, self.key1)

        after_swap = self.swap(arr1, len(arr1) // 2)

        arr2 = self.function(after_swap, self.key2)

        ciphertext = [arr2[self.IP_inv[i] - 1] for i in range(8)]

        return ciphertext

    def binary_(self, val):
        return f"{val:02b}"

    def function(self, ar, key_):
        l = ar[:4]
        r = ar[4:]

        ep = [r[self.EP[i] - 1] for i in range(8)]

        ar = [key_[i] ^ ep[i] for i in range(8)]

        l_1 = ar[:4]
        r_1 = ar[4:]

        row = int(f"{l_1[0]}{l_1[3]}", 2)
        col = int(f"{l_1[1]}{l_1[2]}", 2)
        val = self.S0[row][col]
        str_l = self.binary_(val)

        row = int(f"{r_1[0]}{r_1[3]}", 2)
        col = int(f"{r_1[1]}{r_1[2]}", 2)
        val = self.S1[row][col]
        str_r = self.binary_(val)

        r_ = [int(str_l[i]) for i in range(2)] + [int(str_r[i]) for i in range(2)]

        r_p4 = [r_[self.P4[i] - 1] for i in range(4)]

        l = [l[i] ^ r_p4[i] for i in range(4)]

        output = l + r
        return output

    def swap(self, array, n):
        l = array[:n]
        r = array[n:]

        output = r + l
        return output

    def decryption(self, ar):
        arr = [ar[self.IP[i] - 1] for i in range(8)]

        arr1 = self.function(arr, self.key2)

        after_swap = self.swap(arr1, len(arr1) // 2)

        arr2 = self.function(after_swap, self.key1)

        decrypted = [arr2[self.IP_inv[i] - 1] for i in range(8)]

        return decrypted

if __name__ == "__main__":
    obj = Simple_DES()

    obj.key_generation()

    plaintext = [1, 0, 0, 1, 0, 1, 1, 1] 

    print("\nYour plain Text is:")
    print(*plaintext)

    ciphertext = obj.encryption(plaintext)

    print("\nYour cipher Text is:")
    print(*ciphertext)

    decrypted = obj.decryption(ciphertext)

    print("\nYour decrypted Text is:")
    print(*decrypted)
