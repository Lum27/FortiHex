// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecurityLog {
    mapping(bytes32 => bool) private logEntries;

    function storeLog(bytes32 logHash) public {
        require(!logEntries[logHash], "Log already exists");
        logEntries[logHash] = true;
    }

    function verifyLog(bytes32 logHash) public view returns (bool) {
        return logEntries[logHash];
    }
}
