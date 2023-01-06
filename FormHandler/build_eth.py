from web3 import Web3

latest = web3.eth.blockNumbe.remove()
print(latest)

print(web3.eth.getBlock(latest))

for i in range(0, 10):
    print(web3.eth.getBlock(latest - i))

hash = '0x390297fAA77EF9311d83E8Dd55b7aAb5796Ac4E4'
print(web3.eth.getTransactionByBlock(hash, 2))