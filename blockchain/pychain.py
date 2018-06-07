import pandas as pd
import time
import binascii

class bc():
    def __init__(self):
        self.chain = pd.DataFrame({'Data':[], 'Nonce':[], 'Prev Hash':[], 'Hash':[]})
        
    def mine(self, index = -1, match = '222'):
        """Mine a single block.

        :param blockchain: the blockchain dataframe
        :param index: index to mine, default to last item
        """
        
        start = time.time()
        if (index == -1):
            index = self.chain.shape[0]
        
        data_hash = 0
        
        while (str(data_hash)[:len(match)] != match):
            self.chain.loc[index, 'Nonce']+=1
            nonce = self.chain.loc[index, 'Nonce']
            data_guess = self.chain.loc[index,'Data'] + str(nonce) + str(self.chain.loc[index, 'Prev Hash'])
            data_hash = binascii.crc32(data_guess.encode('utf-8'))
            
        self.chain.loc[index,'Hash'] = data_hash
        diff = time.time() - start
        return diff

    def addBlock(self, data, mining = True):
        """Add a block to the blockchain.

        :param blockchain: the blockchain dataframe
        :param data: data to add to the blockchain
        :param mining: whether to mine the added block or not
        """
        index = self.chain.shape[0]+1
        
        if (index == 1):
            self.chain.loc[index] = [data, 0, 0000000000, 0]
        else:
            self.chain.loc[index] = [data, 0, self.chain.loc[index-1]['Hash'],0]
        if mining:
            self.mine()

    def rehash(self):
        """Rehashes a blockchain dataframe.

        :param blockchain: the blockchain dataframe
        :returns: the rehashed blockchain dataframe
        """

        start = time.time()
        for index, row in self.chain.iterrows():
            if (index == 1):
                data_guess = self.chain.loc[index,'Data'] + str(self.chain.loc[index,'Nonce']) + str(0.0)
                data_hash = binascii.crc32(data_guess.encode('utf-8'))
                self.chain.loc[index,'Hash']=data_hash
            else:
                self.chain.loc[index,'Prev Hash']=self.chain.loc[index-1,'Hash']
                data_guess = self.chain.loc[index,'Data'] + str(self.chain.loc[index, 'Nonce']) + str(self.chain.loc[index, 'Prev Hash'])
                data_hash = binascii.crc32(data_guess.encode('utf-8'))
                self.chain.loc[index,'Hash'] = data_hash
        diff = time.time() - start
        return diff

    def getchain(self):
        """Returns the full blockchain
        :returns: the blockchain dataframe
        """
        return self.chain
        
