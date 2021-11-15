import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei')


def are_we_connected():
    return web3_connection.isConnected()


def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)


def transfer_ETH(sender, receiver, signature, amount_ETH):
    transaction_body = {
        'nonce': get_nonce(sender),
        'to': receiver,
        'value': web3_connection.toWei(amount_ETH, 'ether'),
        'gas': global_gas,
        'gasPrice': global_gas_price
    }
    signed_transaction = web3_connection.eth.account.sign_transaction(transaction_body, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result


print(are_we_connected())
a = transfer_ETH(os.environ['ADDRESS_2'], os.environ['ADDRESS_1'], os.environ['PRIVATE_KEY_2'], 2)
print(a)
# print(a.decode('utf-32-be'))

#0x45cb35a6d08a2dd1ad085ba1a32a3511ca11f152e9b2b53536196e44aada7db3
