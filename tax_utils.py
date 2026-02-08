"""
Tax Utilities - Finance Demo.
Test Type: Deduction Logic

This file demonstrates safe tax calculation logic, ensuring that
calculated tax amounts do not violate basic financial invariants
(non-negative).
"""

from typing import List

def calculate_total_tax(incomes: List[int], taxRatePercent: int) -> int:
    """
    Calculate the total tax for a list of incomes based on a flat rate.
    
    @requires: taxRatePercent >= 0
    @requires: taxRatePercent <= 100
    @ensures: result >= 0
    
    Demonstrates: Percentage calculations and bounds checking.
    Argus validates that the tax calculation (multiplication and division) 
    maintains non-negativity given positive inputs.
    """
    totalTax = 0
    for income in incomes:
        if income > 0:
            # Calculate tax: (income * rate) / 100
            tax = (income * taxRatePercent) // 100
            totalTax = totalTax + tax
    return totalTax

def estimate_retained_income(incomes: List[int], fixedTax: int) -> int:
    """
    Estimate total retained income after a fixed tax deduction per entry.
    
    @requires: fixedTax >= 0
    @ensures: result >= 0
    
    Demonstrates: Subtraction with safety checks.
    """
    totalRetained = 0
    for income in incomes:
        if income > fixedTax:
            retained = income - fixedTax
            totalRetained = totalRetained + retained
    return totalRetained
