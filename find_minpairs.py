import json
import sys

a = sys.argv[1]
b = sys.argv[2]

cmu = json.load(open('cmudict.json'))

pron2word = dict([ (tuple(p), w) for w,p in cmu.items()])

a_words = tuple([(w,p) for w,p in cmu.items() if a in p if len(p) < 6])

b_words = []

good = []

for w,p in a_words:
  n = p.index(a) 
  p2 = p[:]
  p2[n] = a 
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
