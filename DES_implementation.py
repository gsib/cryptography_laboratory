#Globals
IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
      
    
IPI = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    
P1 = [
        56, 48, 40, 32, 24, 16,  8,
         0, 57, 49, 41, 33, 25, 17,
         9,  1, 58, 50, 42, 34, 26,
        18, 10,  2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
         6, 61, 53, 45, 37, 29, 21,
        13,  5, 60, 52, 44, 36, 28,
        20, 12,  4, 27, 19, 11,  3
    ]

P2 = [
        13, 16, 10, 23,  0,  4,
         2, 27, 14,  5, 20,  9,
        22, 18, 11,  3, 25,  7,
        15,  6, 26, 19, 12,  1,
        40, 51, 30, 36, 46, 54,
        29, 39, 50, 44, 32, 47,
        43, 48, 38, 55, 33, 52,
        45, 41, 49, 35, 28, 31
    ]

ShiftTable = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

ExpansionTable = [
        31,  0,  1,  2,  3,  4,
         3,  4,  5,  6,  7,  8,
         7,  8,  9, 10, 11, 12,
        11, 12, 13, 14, 15, 16,
        15, 16, 17, 18, 19, 20,
        19, 20, 21, 22, 23, 24,
        23, 24, 25, 26, 27, 28,
        27, 28, 29, 30, 31,  0		
    ]

P3 = [
        15,  6, 19, 20, 28, 11, 27, 16, 
         0, 14, 22, 25,  4, 17, 30,  9, 
         1,  7, 23, 13, 31, 26,  2,  8,
        18, 12, 29,  5, 21, 10,  3, 24		
    ]

def BintoDec(binstring):
    radix = 1
    val = 0
    for i in range(len(binstring)-1, -1, -1):
        val = val + int(binstring[i])*radix
        radix = radix * 2
    return val

def DectoBin(num):
    num = int(num)
    string = ''
    while(num > 0):
        string = string + str(num%2)
        num = num/2
    string = string[::-1]
    while(len(string) < 4):
        string = '0' + string
    return string

SBoxes = [
        # S1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

        # S2
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

        # S3
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

        # S4
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

        # S5
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

        # S6
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

        # S7
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
	]

def HextoBin(hexstring):
    string = ''
    for i in range(len(hexstring)):
        if(hexstring[i] == '0'):
            string = string + '0000'
            continue
        elif(hexstring[i] == '1'):
            string = string + '0001'
            continue
        elif(hexstring[i] == '2'):
            string = string + '0010'
            continue
        elif(hexstring[i] == '3'):
            string = string + '0011'
            continue
        elif(hexstring[i] == '4'):
            string = string + '0100'
            continue
        elif(hexstring[i] == '5'):
            string = string + '0101'
            continue
        elif(hexstring[i] == '6'):
            string = string + '0110'
            continue
        elif(hexstring[i] == '7'):
            string = string + '0111'
            continue
        elif(hexstring[i] == '8'):
            string = string + '1000'
            continue
        elif(hexstring[i] == '9'):
            string = string + '1001'
            continue
        elif(hexstring[i] == 'A'):
            string = string + '1010'
            continue
        elif(hexstring[i] == 'B'):
            string = string + '1011'
            continue
        elif(hexstring[i] == 'C'):
            string = string + '1100'
            continue
        elif(hexstring[i] == 'D'):
            string = string + '1101'
            continue
        elif(hexstring[i] == 'E'):
            string = string + '1110'
            continue
        elif(hexstring[i] == 'F'):
            string = string + '1111'
            continue
        else:
            print "Invalid Character. Exiting..."
            break
    return string

def BintoHex(bitstring):
    string = ''
    for i in range(len(bitstring)/4):
        if(bitstring[4*i:4*i+4] == '0000'):
            string = string + '0'
            continue
        elif(bitstring[4*i:4*i+4] == '0001'):
            string = string + '1'
            continue
        elif(bitstring[4*i:4*i+4] == '0010'):
            string = string + '2'
            continue
        elif(bitstring[4*i:4*i+4] == '0011'):
            string = string + '3'
            continue
        elif(bitstring[4*i:4*i+4] == '0100'):
            string = string + '4'
            continue
        elif(bitstring[4*i:4*i+4] == '0101'):
            string = string + '5'
            continue
        elif(bitstring[4*i:4*i+4] == '0110'):
            string = string + '6'
            continue
        elif(bitstring[4*i:4*i+4] == '0111'):
            string = string + '7'
            continue
        elif(bitstring[4*i:4*i+4] == '1000'):
            string = string + '8'
            continue
        elif(bitstring[4*i:4*i+4] == '1001'):
            string = string + '9'
            continue
        elif(bitstring[4*i:4*i+4] == '1010'):
            string = string + 'A'
            continue
        elif(bitstring[4*i:4*i+4] == '1011'):
            string = string + 'B'
            continue
        elif(bitstring[4*i:4*i+4] == '1100'):
            string = string + 'C'
            continue
        elif(bitstring[4*i:4*i+4] == '1101'):
            string = string + 'D'
            continue
        elif(bitstring[4*i:4*i+4] == '1110'):
            string = string + 'E'
            continue
        elif(bitstring[4*i:4*i+4] == '1111'):
            string = string + 'F'
            continue
        else:
            print "Invalid Character. Exiting..."
            break
    return string
        


def LeftShift(string, n):
    if(n >= len(string)):
        n = n%len(string)
    return string[n:] + string[0:n]

def swap(string):
    n = len(string)
    return string[n/2:] + string[0:n/2] 

def RoundKeyGenerator(KeyWithParities):
    KeyWithParities = HextoBin(KeyWithParities)
    #CipherKey = KeyWithParities[0:7] + KeyWithParities[8:15] + KeyWithParities[16:23] + KeyWithParities[24:31] \
    #           + KeyWithParities[32:39] + KeyWithParities[40:47] + KeyWithParities[48:57] + KeyWithParities[56:63]

    CipherKey = ''
    for i in range(len(P1)):
        CipherKey = CipherKey + KeyWithParities[P1[i]]

    RoundKeys = []
    for i in range(16):
        temp1 = LeftShift(CipherKey[0:28], ShiftTable[i])
        temp2 = LeftShift(CipherKey[28:56], ShiftTable[i])
        CipherKey = temp1 + temp2

        RoundKey = ''
        for j in range(len(P2)):
            RoundKey = RoundKey + CipherKey[P2[j]]
        RoundKeys.append(BintoHex(RoundKey))
    return RoundKeys
    
def ip(Ri):
    Ri = HextoBin(Ri)
    PermutedRi = ''
    for i in range(len(IP)):
        PermutedRi = PermutedRi + Ri[IP[i] - 1]
    return(BintoHex(PermutedRi))
    
def ipi(Ri):
    Ri = HextoBin(Ri)
    PermutedRi = ''
    for i in range(len(IPI)):
        PermutedRi = PermutedRi + Ri[IPI[i] - 1]
    return(BintoHex(PermutedRi))
    
def f(Ri, Ki):
    Ri = HextoBin(Ri)
    Ki = HextoBin(Ki)
    ExpandedRi = ''
    for i in range(len(ExpansionTable)):
        ExpandedRi = ExpandedRi + Ri[ExpansionTable[i]]
    temp = ''
    
    for i in range(len(ExpandedRi)):
        temp = temp + str(int(ExpandedRi[i]) ^ int(Ki[i]))

    Substituted = ''
    for i in range(len(temp)/6):
        row = temp[6*i] + temp[6*i + 5]
        col = temp[6*i+1:6*i+5]
        row = BintoDec(row)
        col = BintoDec(col)
        val = SBoxes[i][row*16 + col]
        Substituted = Substituted + DectoBin(val)

    Permuted = ''
    for i in range(len(Substituted)):
        Permuted = Permuted + Substituted[P3[i]]

    return BintoHex(Permuted)

def Mixer(A, B):
##    print "A: "+ A
##    print "B: "+ B
    A = HextoBin(A)
    B = HextoBin(B)
    temp = ''
    for i in range(len(A)):
        temp = temp + str(int(A[i]) ^ int(B[i]))

    return BintoHex(temp)

if __name__ == "__main__":
    Plaintext = str(raw_input("Enter the text : "))
    #Plaintext = ""
    Key = "AABB09182736CCDD"
    RoundKeys =  RoundKeyGenerator(Key)

    print "Encrypting..."
    
    Ciphertext = ip(Plaintext)
    for i in range(16):
        L0 = Ciphertext[0:8]
        R0 = Ciphertext[8:16] 
        temp = f(R0, RoundKeys[i])
        #print temp
        L0 = Mixer(L0, temp)
        print "Left : " + R0, 
        print "Right: " + L0,
        print "RoundKey: " + RoundKeys[i]
        #print L0
        Ciphertext = R0 + L0
    Ciphertext = ipi(swap(Ciphertext))
    print "Ciphertext: " + Ciphertext

    print "Decrpyting..."

    Ciphertext = ip(Ciphertext)
    print Ciphertext
    for i in range(16):
        L0 = Ciphertext[0:8]
        R0 = Ciphertext[8:16] 
        temp = f(R0, RoundKeys[15 - i])
        #print temp
        L0 = Mixer(L0, temp)
        print "Left : " + R0, 
        print "Right: " + L0,
        print "RoundKey: " + RoundKeys[15 - i]
        #print L0
        Ciphertext = R0 + L0

    print "Plaintext: " + ipi(swap(Ciphertext))
