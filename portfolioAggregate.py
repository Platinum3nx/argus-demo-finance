"""
Portfolio Aggregate - Finance Demo.
Test Type: Loop-Based Aggregation

This file demonstrates Argus's new Dafny backend ensuring that
accumulated values (sums, totals) maintain safety properties (non-negativity)
even when iterating over lists of unknown size.
"""

from typing import List

def calculate_daily_total(transactions: List[int]) -> int:
    """
    Sum all transactions for the day.
    
    @requires: True
    @ensures: result >= 0
    
    Demonstrates: Simple accumulation with a safety filter.
    Argus automatically generates the loop invariant `invariant total >= 0`.
    """
    total = 0
    for amount in transactions:
        # Safety: Ignore negative values (failed transactions or refunds)
        # Without this check, the total could become negative!
        if amount > 0:
            total = total + amount
    return total

def calculate_interest_batch(balances: List[int], rateBps: int) -> int:
    """
    Calculate total interest payout for a batch of accounts.
    
    @requires: rateBps >= 0
    @ensures: result >= 0
    
    Demonstrates: arithmetic operations inside a loop.
    rateBps is basis points (1/10000).
    """
    totalInterest = 0
    for balance in balances:
        if balance > 0:
            # Integer arithmetic: (balance * rate) // 10000
            interest = (balance * rateBps) // 10000
            if interest > 0:
                totalInterest = totalInterest + interest
    return totalInterest
