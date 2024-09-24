def convert_currency(amount, from_currency, to_currency):
    # This function should call a real-world API or use mock data
    # For simplicity, we'll use fixed rates here for the example
    conversion_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75},
        'EUR': {'USD': 1.18, 'GBP': 0.88},
        'GBP': {'USD': 1.33, 'EUR': 1.14}
    }
    
    rate = conversion_rates.get(from_currency, {}).get(to_currency, 1)
    return amount * rate
