// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract GetSet{
    string public message;
    
    function Get() view public returns(string memory){
        return  message;
    }

    function Set(string memory _msg) public {
        message = _msg;
    }
}