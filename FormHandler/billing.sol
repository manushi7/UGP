// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Billing {

    struct details {
        uint256 total_charge;
        uint256 amount_paid;
        uint256 balance_due;
    }

    mapping(uint256 => details) public billing_details;

    
    constructor() {
    }


    function add_details(uint256 id, uint256 total_charge,uint256 amount_paid,
        uint256 balance_due) public {
            billing_details[id].total_charge = total_charge;
            billing_details[id].amount_paid = amount_paid;
            billing_details[id].balance_due = balance_due;  
    }

    function get_details(uint256 id) public view returns(details memory billing_detail) {
      return billing_details[id];
    }

}