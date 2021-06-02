from user_data.strategies.EMACross import EMACross


class EMACross4h(EMACross):
    # Use Custom Stop loss?
    use_custom_stoploss = True

    # Optimal timeframe for the strategy
    timeframe = '4h'

    # Moving Average Rolling Windows
    ma_short_window = 20
    ma_long_window = 60

