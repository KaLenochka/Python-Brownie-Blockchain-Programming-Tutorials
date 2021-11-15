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
contract_address = os.environ['CONTRACT_ADDRESS']


def get_balance():
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    balance_contract = web3_connection.fromWei(contract.functions.getBalance().call(), 'ether')
    return balance_contract


def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)


def play(player, guess, amount_ETH, signature):
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    transaction_body = {
        'nonce': get_nonce(player),
        'value': web3_connection.toWei(amount_ETH, 'ether')
    }
    function_call = contract.functions.play(player, guess).buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(function_call, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result


print(are_we_connected())
print(play(os.environ['ADDRESS_2'], 7, 1, os.environ['PRIVATE_KEY_2']))
print(get_balance())
