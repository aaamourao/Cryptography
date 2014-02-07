#
#	AES on CTR implementation
#
#	Adriano de Araujo Abreu Mourao (mourao.aaa@gmail.com)
#

from Crypto.Cipher import AES
import Crypto.Util.Counter

ciphers	= ["69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3" + \
		"88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329", \
		"770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa" + \
		"0e311bde9d4e01726d3184c34451"]

key 	= "36f18357be4dbd77f050515c73fcf9f2" 

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

class IVCounter(object):
	def __init__(self, value):
		self.IV = value

	def increment(self):
		# Add the counter value to IV
		newIV = hex(int(self.IV.encode('hex'), 16) + 1)
		
		# Cut the negligible part of the string
		return  str(newIV[2:len(newIV)].decode('hex')) # for not L strings remove $ - 1 $ 

def ctr(cipher):
	# Split the CT in blocks of 16 bytes
	blocks = split_len(cipher.decode('hex'), 16)

	# Takes the initiator vector
	IV = blocks[0]
	blocks.remove(IV)

	# ctr_e = Crypto.Util.Counter.new(128, initial_value=long(IV.encode('hex'), 16))
	# decryptor = AES.new(key.decode('hex'), AES.MODE_CTR, counter=ctr_e)
	# print decryptor.decrypt(''.join(blocks))

	# Message block 
	msg = []

	# Decrypt
	counter = 0
	for b in blocks:
		# Add the counter value to IV
		newIV = hex(int(IV.encode('hex'), 16) + counter)

		# Cut the negligible part of the string
		newIV = newIV[2:len(newIV)-1].decode('hex')

		# Counter the new iteration
		counter = counter + 1

		# Decrypt AES on CTR mode
		aes = decrypt(key.decode('hex'), newIV)
		msg.append(strxor(b, aes))


	return msg

def main():
	for c in ciphers:
		print 'msg = ' + ''.join(ctr(c))

if __name__ == '__main__':
	iv = IVCounter("0000")
	print IVCounter.increment(iv)
	print IVCounter.increment(iv)

