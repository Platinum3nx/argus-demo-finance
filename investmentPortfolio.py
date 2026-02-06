"""
Investment Portfolio Manager

Handles basic stock operations with safety checks.
"""

def buy_stock(portfolio: dict, symbol: str, quantity: int, price: int) -> dict:
    """
    Add stock to portfolio.
    
    Safety:
    - quantity > 0
    - price > 0
    """
    if quantity <= 0 or price <= 0:
        return portfolio
    
    # Create a shallow copy to ensure immutability of the input portfolio
    new_portfolio = portfolio.copy()
    
    # Safe retrieval of current state or default initialization
    current_data = new_portfolio.get(symbol, {'quantity': 0, 'avg_cost': 0})
    current_qty = current_data['quantity']
    current_cost = current_data['avg_cost']
    
    # Weighted average cost basis calculation
    total_cost = (current_qty * current_cost) + (quantity * price)
    new_qty = current_qty + quantity
    
    # Assign new dictionary to the symbol to avoid mutating shared inner state
    new_portfolio[symbol] = {
        'quantity': new_qty,
        'avg_cost': total_cost // new_qty
    }
    
    return new_portfolio


def sell_stock(portfolio: dict, symbol: str, quantity: int, price: int) -> dict:
    """
    Remove stock from portfolio.
    
    Safety:
    - quantity > 0
    - price > 0
    - Cannot sell more than owned
    """
    if quantity <= 0 or price <= 0:
        return portfolio
        
    if symbol not in portfolio:
        return portfolio
        
    current_data = portfolio[symbol]
    current_qty = current_data['quantity']
    
    if quantity > current_qty:
        return portfolio # Reject overdraft
        
    new_qty = current_qty - quantity
    
    # Create a shallow copy to ensure immutability of the input portfolio
    new_portfolio = portfolio.copy()
    
    if new_qty == 0:
        if symbol in new_portfolio:
            del new_portfolio[symbol]
    else:
        # Create new data dict to avoid mutating original inner dict
        new_portfolio[symbol] = {
            'quantity': new_qty,
            'avg_cost': current_data['avg_cost']
        }
        
    return new_portfolio


def calculate_portfolio_value(portfolio: dict, current_prices: dict) -> int:
    """
    Get total portfolio value in cents.
    
    Safety:
    - prices >= 0
    """
    total_value = 0
    
    for symbol, data in portfolio.items():
        # Defensive programming for safe access
        qty = data.get('quantity', 0)
        price = current_prices.get(symbol, 0)
        
        if price < 0:
            continue # Skip invalid prices
            
        total_value += qty * price
        
    return total_value