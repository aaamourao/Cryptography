#
#	AES on CBC implementation
#
#	Adriano de Araujo Abreu Mourao (mourao.aaa@gmail.com)
#

from Crypto.Cipher import AES

ciphers	= ["4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee" + \
		"2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81", \
		"5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48" + \
		"e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"]

key 	= "140b41b22a29beb4061bda66b6747e14" 

def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def split_len(seq, lenght):
	return [seq[i:i+lenght] for i in range(0, len(seq), lenght)]

def decrypt(k, cipher):
	decryptor = AES.new(k, AES.MODE_ECB)

	return decryptor.decrypt(cipher)

def cbc(cipher):
	# Split the CT in blocks of 16 bytes
	blocks = split_len(cipher.decode('hex'), 16)

	# Takes the nitiator vector
	IV = blocks[0]
	blocks.remove(IV)

	# Message block 
	msg = []
	
	# Decrypt
	last_round = IV
	for b in blocks:
		msg.append(strxor(decrypt(key.decode('hex'), b), last_round))
		last_round = b	

	return msg

def main():
	for c in ciphers:
		print ''.join(cbc(c))

if __name__ == '__main__':
	main()


