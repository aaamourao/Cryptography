#
#	Question 7 Week 1
#
#	Adriano de Araujo Abreu Mourao
#

def codeBreaker():
	message = 'attack at dawn'
	crptedMsg = '6c73d5240a948c86981bc294814d'.decode('hex')

	key = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(message, crptedMsg))
	
	return key

def stringXOR(s1, s2):

	return ''.join(chr(ord(a) ^ord(b)) for a,b in zip(s1, s2))

if __name__ == '__main__':

	print stringXOR('attack at dusk', codeBreaker()).encode('hex')
