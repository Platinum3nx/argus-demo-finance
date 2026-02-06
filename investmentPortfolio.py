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
    
    # Init symbol if new
    if symbol not in portfolio:
        portfolio[symbol] = {'quantity': 0, 'avg_cost': 0}
        
    current_qty = portfolio[symbol]['quantity']
    current_cost = portfolio[symbol]['avg_cost']
    
    # Weighted average cost basis
    total_cost = (current_qty * current_cost) + (quantity * price)
    new_qty = current_qty + quantity
    
    portfolio[symbol]['quantity'] = new_qty
    portfolio[symbol]['avg_cost'] = total_cost // new_qty
    
    return portfolio


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
        
    current_qty = portfolio[symbol]['quantity']
    
    if quantity > current_qty:
        return portfolio # Reject overdraft
        
    new_qty = current_qty - quantity
    
    if new_qty == 0:
        del portfolio[symbol]
    else:
        portfolio[symbol]['quantity'] = new_qty
        # avg_cost doesn't change on sell
        
    return portfolio


def calculate_portfolio_value(portfolio: dict, current_prices: dict) -> int:
    """
    Get total portfolio value in cents.
    
    Safety:
    - prices >= 0
    """
    total_value = 0
    
    for symbol, data in portfolio.items():
        qty = data['quantity']
        price = current_prices.get(symbol, 0)
        
        if price < 0:
            continue # Skip invalid prices
            
        total_value += qty * price
        
    return total_value
