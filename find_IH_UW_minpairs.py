import json
cmu = json.load(open('cmudict.json'))

pron2word = dict([ (tuple(p), w) for w,p in cmu.items()])

IH1 = [(w,p) for w,p in cmu.items() if 'IH1' in p if len(p) < 6]

UW1 = []

good = []

for w,p in IH1:
  n = p.index('IH1') 
  p2 = p[:]
  p2[n] = 'UW1'
  p2 = tuple(p2)
  if p2 in pron2word:
    good.append( [w,p, pron2word[p2], p2] )
  

for w,p, w2, p2 in sorted(good):
  print w,p, '\n', w2, p2, '\n'

"""
UW1 = [(w,p) for w,p in cmu.items() if 'UW1' p if len(p) < 6]

for w, p in cmu.items():
  if p.replace("IH1", "UW1") in cmu:
    print w, p, cmu[p.replace("IH1", "UW1")], cmu[p.replace("IH1", "UW1")]

for w, p in cmu.items():
  if p.replace("IH1", "UW1") in cmu:
    pass
"""
