from web3 import Web3

public_key = "0x56483813760f61689B00D8f0A1FA8B0380d1248F"
private_key = "07ebbeda5a07a09ff3f4581b17f88dbbfd08339e52f79258c04eb9613da91898"

url = 'https://goerli.infura.io/v3/371fea331bbb427fb214b1c8591fdc13'
w3 = Web3(Web3.HTTPProvider(url))

address = w3.toChecksumAddress("0xe35D3aeae44cF0aa8d587b82faa423aB0B340f8f")
abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "total_charge",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amount_paid",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "balance_due",
				"type": "uint256"
			}
		],
		"name": "add_details",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "billing_details",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "total_charge",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amount_paid",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "balance_due",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "get_details",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "total_charge",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "amount_paid",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "balance_due",
						"type": "uint256"
					}
				],
				"internalType": "struct Billing.details",
				"name": "billing_detail",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
# calls contract functions
contract = w3.eth.contract(address=address,abi=abi)

def add_details( id,  total_charge, amount_paid,
         balance_due):
    tx = contract.functions.add_details(id,  total_charge, amount_paid,
         balance_due).buildTransaction(
    {
        'from': public_key,
        'nonce': w3.eth.get_transaction_count(public_key),
    })
    tx_create = w3.eth.account.sign_transaction(tx, private_key)


    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    



def get_details(id):
    return (contract.functions.get_details(id).call())

