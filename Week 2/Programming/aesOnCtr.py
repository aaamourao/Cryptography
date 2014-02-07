#
#	AES on CTR implementation
#
#	Adriano de Araujo Abreu Mourao (mourao.aaa@gmail.com)
#

from Crypto.Cipher import AES

ciphers	= ["69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3" + \
		"88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329", \
		"770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa" + \
		"0e311bde9d4e01726d3184c34451"]

key 	= "36f18357be4dbd77f050515c73fcf9f2"  

class IVCounter(object):
	def __init__(self, value):
		self.value = value
		
	def increment(self):
		# Add the counter value to IV
		newIV = hex(int(self.value.encode('hex'), 16) + 1)
		
		# Cut the negligible part of the string
		self.value = newIV[2:len(newIV) - 1].decode('hex') # for not L strings remove $ - 1 $ 
		return self.value

	def __repr__(self):
		self.increment()
		return self.value

	def string(self):
		return self.value

class CTR():
	def __init__(self, k):
		self.key = k.decode('hex')

	def __strxor(self, a, b):     # xor two strings of different lengths
		if len(a) > len(b):
			return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
		else:
			return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

	def __split_len(self, seq, lenght):
		return [seq[i:i+lenght] for i in range(0, len(seq), lenght)]

	def __AESencryptor(self, cipher):
		encryptor = AES.new(self.key, AES.MODE_ECB)

		return encryptor.encrypt(cipher)

	def decrypt(self, cipher):
		# Split the CT into blocks of 16 bytes
		blocks = self.__split_len(cipher.decode('hex'), 16)

		# Takes the initiator vector
		self.IV = IVCounter(blocks[0])
		blocks.remove(blocks[0])	

		# Message block 
		msg = []

		# Decrypt
		for b in blocks:
			aes = self.__AESencryptor(self.IV.string())
			msg.append(self.__strxor(b, aes))

			self.IV.increment()

		return ''.join(msg)

def main():
	decryptor = CTR(key)
	for c in ciphers:
		print 'msg = ' + decryptor.decrypt(c)

if __name__ == '__main__':
	main()

