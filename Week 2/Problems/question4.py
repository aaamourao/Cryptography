#
#	Question 4, Week 2 Quiz
#
#	Adriano Mourao (mouraa dot aaa at gmail dot com)
#

ciphersPairs = [["2d1cfa42c0b1d266","eea6e3ddb2146dd0"],
		["5f67abaf5210722b","bbe033c00bc9330e"],
		["e86d2de2e1387ae9","1792d21db645c008"],
		["4af532671351e2e1","87a40cfa8dd39154"]]

def stringXOR(s1, s2):

	return ''.join(chr(ord(a) ^ord(b)) for a,b in zip(s1, s2))

def main():
	for [c1, c2] in ciphersPairs:
		xored = stringXOR(c1.decode('hex'), c2.decode('hex')).encode('hex')
		print xored[:8] + ' ' + xored[8:] 

if __name__ == '__main__':
	main()
