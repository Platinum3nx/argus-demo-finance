"""
Audit Logger - Finance Demo.
Test Type: Sequence Validation

This file demonstrates Argus verifying event sequences and counting logic,
ensuring that audit logs are consistent and event counts are non-negative.
"""

from typing import List

def countHighValueEvents(amounts: List[int], threshold: int) -> int:
    """
    Count the number of events exceeding a value threshold.
    
    @requires: threshold >= 0
    @ensures: result >= 0
    
    Demonstrates: Conditional counting in a loop.
    Argus ensures the counter remains non-negative.
    """
    if threshold < 0:
        threshold = 0
    
    count = 0
    for amount in amounts:
        # Safety check: only count valid positive amounts
        if amount > threshold:
            count = count + 1
    return count

def validateEventSequence(eventCodes: List[int]) -> int:
    """
    Validate a sequence of event codes.
    
    @requires: True
    @ensures: result >= 0
    
    Returns 1 if sequence is valid, 0 otherwise.
    Rule: Event 5 (Error) must be followed by Event 9 (Resolution).
    """
    pendingError = 0
    
    for code in eventCodes:
        if code == 5:
            if pendingError == 1:
                return 0 # Error followed by error without resolution
            pendingError = 1
        elif code == 9:
            if pendingError == 0:
                return 0 # Resolution without error
            pendingError = 0
    
    # unmatched error at end
    if pendingError == 1:
        return 0
        
    return 1
