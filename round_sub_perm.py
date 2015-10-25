# Assignment 7 
# Substitution + Permutation Rounds
# Author : Suman Sahu
# Roll No.: 712CS2151
# Compiler : Python 3.x

# Defining the substitution box[S-Box]
s_box = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
# Defining the permutation box[P-Box]
p_box = [0, 3, 4, 6, 2, 5, 1, 7]
# Defining reverse S-Box and P-Box for decryption
reverse_s_box = [14, 3, 4, 8, 1, 12, 10, 15, 7, 13, 9, 6, 11, 2, 0, 5]
reverse_p_box = [0, 6, 4, 1, 2, 5, 3, 7]
round_key = "11011011010101101101101101011010"

# Encryption Logic

# Permutation Round 
def permute(text):
	t = ''
	for i in range(8):
		t+=str(text[p_box[i]])
	return t

# Substitution Round
def substitute(text):
	t1 = int(text[0:4],2)
	t2 = int(text[4:],2)
	t1 = str(format(s_box[t1],'#06b'))[2:]
	t2 = str(format(s_box[t2],'#06b'))[2:]
	return t1+t2

def round(r,text,r_key):
	t = ''
	for i in range(8):
		t += str(int(text[i])^int(r_key[i]))
	print("After XORing       : ",end='')
	print(t)
	t = substitute(t)
	print("After Substitution : ",end='')
	print(t)
	t = permute(t)
	print("After Permutation  : ",end='')
	print(t)
	print("After Round {0}      : ".format(r+1), end='')
	print(t)
	print("\n")
	return t

def encrypt():
	plain_text = "10110101"
	print("Encryption :")
	print("Plain Text         : ",end='')
	print(plain_text)
	print("\n")
	t = plain_text
	for i in range(4): 
		print("Round #{0} key       : {1}".format(i+1,round_key[8*i:8*i+8]))
		t = round(i,t,round_key[8*i:8*i+8])
	return t

# Decryption Logic

# Reverse Permutation
def r_permute(text):
	t = ''
	for i in range(8):
		t+=str(text[reverse_p_box[i]])
	return t

# Reverse Substitution
def r_substitute(text):
	t1 = int(text[0:4],2)
	t2 = int(text[4:],2)
	t1 = str(format(reverse_s_box[t1],'#06b'))[2:]
	t2 = str(format(reverse_s_box[t2],'#06b'))[2:]
	return t1+t2

# Reverse Round
def r_round(r,text,r_key):
	text = r_permute(text)
	print("After Permutation  : ",end='')
	print(text)
	text = r_substitute(text)
	print("After Substitution : ",end='')
	print(text)
	t = ''
	for i in range(8):
		t += str(int(text[i])^int(r_key[i]))
	print("After XORing       : ",end='')
	print(t)
	text = t
	if(r==3):
		text = r_permute(text)
	print("After Round {0}      : ".format(r+1), end='')
	print(text)
	print("\n")
	return text


def decrypt(cipher_text):
	print("Decryption : ")
	print("CipherText : ",end='')
	print(cipher_text)
	print("\n")
	t = cipher_text
	for i in range(4):
		print("Round #{0} key       : {1}".format(i+1,round_key[8*i:8*i+8]))
		t = r_round(i,t,round_key[8*i:8*i+8])

if __name__=="__main__":
	t = encrypt()
	decrypt(t)