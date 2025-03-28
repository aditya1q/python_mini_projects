def calculate_slippage(signal_price, execution_price, trade_type):
    """
    Calculate slippage based on trade type.
    - For buys: execution_price - signal_price (positive = unfavorable)
    - For sells: signal_price - execution_price (positive = unfavorable)
    """
    if trade_type.lower() == "buy":
        slippage = execution_price - signal_price
    elif trade_type.lower() == "sell":
        slippage = signal_price - execution_price
    else:
        raise ValueError("Invalid trade_type. Use 'buy' or 'sell'.")

    percentage_slippage = (slippage / signal_price) * \
        100 if signal_price != 0 else 0
    return {
        "absolute_slippage": round(slippage, 2),
        "percentage_slippage": round(percentage_slippage, 2)
    }
