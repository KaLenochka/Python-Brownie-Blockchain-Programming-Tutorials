pragma solidity ^0.8.1;
contract guess_number{

    uint secretNumber;

    enum State {ACTIVE, COMPLETE}
    State public currState;
    uint balance;

    constructor (uint _secretNumber) payable {
        require(msg.value >= 10*10**18, 'this contract needs to be funded with 10 ETH');
        secretNumber = _secretNumber;
        balance = msg.value;
    }

    function getBalance() public view returns (uint){
        return balance;
    }

    function play(address payable player, uint _numberGuess) external payable returns (uint) {
        require(msg.value >= 10**18, 'pay at least one ETH to gain');
        require(currState == State.ACTIVE, 'Too late');
        balance = balance+msg.value;
        if (_numberGuess == secretNumber) {
            player.transfer(address(this).balance);
            currState = State.COMPLETE;
            return balance;
        }
        else {
            return balance;
        }
    }
}