// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract LiftingFaceToken is ERC20 {
    constructor(uint256 initialSupply) public ERC20("LiftingFaceToken", "LFT") {
        _mint(msg.sender, initialSupply);
    }
}
