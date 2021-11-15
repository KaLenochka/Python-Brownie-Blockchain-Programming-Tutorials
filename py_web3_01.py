from web3 import Web3

node_provider = 'https://mainnet.infura.io/v3/8dfb054a9cf9472bb6379930bcf841c0'
web3_connection = Web3(Web3.HTTPProvider(node_provider))


def are_we_connected():
    print(web3_connection.isConnected())


def latest_block():
    print(web3_connection.eth.blockNumber)


def balance_of(ETH_address):
    balance = web3_connection.eth.get_balance(ETH_address)
    balance_ETH = web3_connection.fromWei(balance, 'ether')
    print(balance_ETH)


are_we_connected()
latest_block()
balance_of('0x5A0b54D5dc17e0AadC383d2db43B0a0D3E029c4c')
