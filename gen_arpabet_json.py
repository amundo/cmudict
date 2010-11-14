import json

lines = [ line for line in open('arpabet.txt','U').read().decode('utf-8').splitlines() if not line.startswith('#')]

rules = [line.split('\t') for line in lines]

open('arpabet.json','w').write( json.dumps([(a.strip(),b.strip(), c.strip()) for a,b,c in rules]).encode('utf-8'))
