#huffman compression.......
def frequency (str) :
     freqs = {}
     for ch in str :
         freqs[ch] = freqs.get(ch,0) + 1
     return freqs
#print frequency("aaabccdeeeeeffg")
def sortFreq(freqs):
     letters = freqs.keys()
     tuples = []
     for let in letters :
         tuples.append((freqs[let],let))
     tuples.sort()
     return tuples
#print sortFreq(frequency("aaabccdeeeeeffg"))
def buildtree(tuples):
	while len(tuples)> 1:
		leasttwo = tuple(tuples[0:2])
		therest = tuples[2:]
		combfreq = leasttwo[0][0] + leasttwo[1][0]
		tuples = therest + [(combfreq,leasttwo)]
		tuples.sort()
	return tuples[0]
#print buildtree( [(1, 'b'), (1, 'd'), (1, 'g'), (2, 'c'), (2, 'f'), (3, 'a'), (5, 'e')]  )
def trimtree(tree):
	p =tree[1]
	if type(p) == type(""):
		return p
	else:
		return trimtree(p[0]),trimtree(p[1])
#print trimtree(buildtree( [(1, 'b'), (1, 'd'), (1, 'g'), (2, 'c'), (2, 'f'), (3, 'a'), (5, 'e')]  ))
codes = {}
def assigncodes(node, pat=''):
	global codes
	if type(node) == type(""):
		codes[node] = pat
	else:	
		assigncodes(node[0],pat+'0')
		assigncodes(node[1],pat+'1')
	return codes
#print assigncodes((('a', ('g', 'c')), (('f', ('b', 'd')), 'e')))
def encode(str):
	global codes
	output = ''
	for ch in str:
		output += codes[ch]
	return output
#print encode("aaabccdeeeeeffg")	
def decode(tree,str):
	output =""
	p = tree
	for bit in str:
		if bit == '0':
			p =p[0]
		else:
			p = p[1]
		if type(p) == type(""):
			output += p
			p = tree
	return output
#print decode((('a', ('g', 'c')), (('f', ('b', 'd')), 'e')),"000000101001101110111111111111100100010")
