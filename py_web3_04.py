import os
import json
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
web3_connection = Web3(Web3.HTTPProvider(node_provider))


def are_we_connected():
    return web3_connection.isConnected()


contract_abi = json.loads(os.environ['CONTRACT_ABI'])
contract_bytecode = os.environ['CONTRACT_BYTECODE']


def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)


def deploy_contract(secret_number, amount_ETH, owner, signature):
    guess_number = web3_connection.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    transaction_body = {
        'nonce': get_nonce(owner),
        'value': web3_connection.toWei(amount_ETH, 'ether')
    }
    deployment = guess_number.constructor(secret_number).buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(deployment, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result


print(are_we_connected())
print(deploy_contract(4, 10, os.environ['ADDRESS_1'], os.environ['PRIVATE_KEY_1']))
