"""
Currency Operations - Finance Demo.
Test Type: Arithmetic Safety

This file demonstrates Argus verifying currency conversion safety
where we must ensure that converting positive amounts results in
positive totals, preventing integer overflow or negative balances.
"""

from typing import List

def convert_currency_batch(amounts: List[int], rate: int) -> int:
    """
    Convert a batch of transaction amounts using a specific exchange rate.
    
    @requires: rate > 0
    @ensures: result >= 0
    
    Demonstrates: Multiplication safety in loops with preconditions.
    Argus proves that with a positive rate and positive amounts, 
    the total converted value remains non-negative.
    """
    totalConverted = 0
    for amount in amounts:
        # Safety: Only convert valid, positive transactions
        if amount > 0:
            converted = amount * rate
            totalConverted = totalConverted + converted
    return totalConverted

def calculate_exchange_fee(amounts: List[int], feePerTx: int) -> int:
    """
    Calculate the total exchange fees for a batch of transactions.
    
    @requires: feePerTx >= 0
    @ensures: result >= 0
    
    Demonstrates: Accumulation of a constant value based on list filtering.
    """
    totalFee = 0
    for amount in amounts:
        if amount > 0:
            totalFee = totalFee + feePerTx
    return totalFee
