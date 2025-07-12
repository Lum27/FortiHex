// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecurityLog {
    struct Log {
        address user;
        string message;
        uint timestamp;
    }

    Log[] public logs;

    function logEvent(string memory message) public {
        logs.push(Log(msg.sender, message, block.timestamp));
    }

    function getLogsCount() public view returns (uint) {
        return logs.length;
    }
}
