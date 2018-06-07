import pandas as pd
import time

import binascii

match = '2222'
blockchain = pd.DataFrame({'Data':[], 'Nonce':[], 'Prev Hash':[], 'Hash':[]})

def mine(index = -1):
    global blockchain
    global match
    start = time.time()
    if (index == -1):
        index = blockchain.shape[0]
    
    data_hash = 0
    
    while (str(data_hash)[:len(match)] != match):
        blockchain.loc[index, 'Nonce']+=1
        nonce = blockchain.loc[index, 'Nonce']
        data_guess = blockchain.loc[index,'Data'] + str(nonce) + str(blockchain.loc[index, 'Prev Hash'])
        data_hash = binascii.crc32(data_guess.encode('utf-8'))
        
    blockchain.loc[index,'Hash'] = data_hash
    end = time.time()
    print('Mine time: '+str(end-start))

def addBlock(data):
    index = blockchain.shape[0]+1
    
    if (index == 1):
        blockchain.loc[index] = [data, 0, 0000000000, 0]
    else:
        blockchain.loc[index] = [data, 0, blockchain.loc[index-1]['Hash'],0]
    mine()

def rehash():
    global blockchain

    start = time.time()
    for index, row in blockchain.iterrows():
        if (index == 1):
            data_guess = blockchain.loc[index,'Data'] + str(blockchain.loc[index,'Nonce']) + str(0.0)
            data_hash = binascii.crc32(data_guess.encode('utf-8'))
            blockchain.loc[index,'Hash']=data_hash
        else:
            blockchain.loc[index,'Prev Hash']=blockchain.loc[index-1,'Hash']
            data_guess = blockchain.loc[index,'Data'] + str(blockchain.loc[index, 'Nonce']) + str(blockchain.loc[index, 'Prev Hash'])
            data_hash = binascii.crc32(data_guess.encode('utf-8'))
            blockchain.loc[index,'Hash'] = data_hash
    end = time.time()
    print('Hash time: '+str(end-start))
        


words = ['this', 'is', 'a', 'blockchain', 'i', 'will', 'keep', 'testing', 'more', 'data', 'can', 'never', 'hurt']

for word in words:
    addBlock(word)

print(blockchain)
print('Attempting rehash')
rehash()
print(blockchain)
print('Changing value')
blockchain.loc[4, 'Data'] = 'Malicious shit'
print(blockchain)
print('Rehashing')
rehash()
print(blockchain)
