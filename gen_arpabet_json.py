import json

lines = [ line for line in open('arpabet.txt','U').read().decode('utf-8').splitlines() if not line.startswith('#')]

rules = [line.split('\t') for line in lines]

rules = [(a.strip(),b.strip(), c.strip()) for a,b,c in rules]

serialized_rules = json.dumps(rules, indent=2).encode('utf-8')

open('arpabet.json','w').write( serialized_rules )
