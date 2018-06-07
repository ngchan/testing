#Import modules

import pychain as pc

bc = pc.bc()        

transaction = 'AB220;CD420;5'

words = ['this', 'is', 'a', 'blockchain', 'i', 'will', 'keep', 'testing', 'more', 'data', 'can', 'never', 'hurt']

for word in words:
    bc.addBlock(word)

#print(bc.blockchain)

#print('Attempting rehash')
#blockchain = rehash(blockchain)
#print(blockchain)
#print('Changing value')
#blockchain.loc[4, 'Data'] = 'Malicious shit'
#print(blockchain)
#print('Rehashing')
#blockchain = rehash(blockchain)
#print(blockchain)


