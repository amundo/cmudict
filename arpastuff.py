from random import choice
from unicodedata import category
from unicodedata import name
import json

arpabet = json.load(open('arpabet.json','U'))
print arpabet
for a,b,c in arpabet: print a,b
exit()

cmu  = [line.strip() for line in open('cmudict.txt','U').read().decode('utf-8').splitlines()]

set([line.count('\t') for line in cmu])

pass
lex = [] 
for line in cmu:
 lex.append( (line.split()[0], line.split()[1:]  )  )
choice(lex)
open('cmu.json','w').write(json.dumps(lex).encode('utf-8'))
rules = [(a.strip(),b.strip(),c.strip()) for a,b,c in rules]

ipalex = [] 
arpabet = [(a,b) for a,b,c in rules]
