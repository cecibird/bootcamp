# to compare the similarity of a sample of words 
import spacy 
nlp = spacy.load('en_core_web_md') 
tokens=nlp("honey snake bees")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text,token2.text, token1.similarity(token2))
'''
The results show that honey and bees have higher similarity, probaby because bees make honey. 
Snake and bees have a slightly higher similarity than snake and honey, as they are both living things.

honey honey 1.0
honey snake 0.3205214738845825
honey bees 0.5766233801841736
snake honey 0.3205214738845825
snake snake 1.0
snake bees 0.37349849939346313
bees honey 0.5766233801841736
bees snake 0.37349849939346313
bees bees 1.0

'''
'''
results from nlp = spacy.load('en_core_web_sm') 
UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token1.text,token2.text, token1.similarity(token2))
honey snake 0.6028896570205688
honey bees 0.17425638437271118
snake honey 0.6028896570205688
snake snake 1.0
snake bees 0.3235456645488739
bees honey 0.17425638437271118
bees snake 0.3235456645488739
bees bees 1.0
'''