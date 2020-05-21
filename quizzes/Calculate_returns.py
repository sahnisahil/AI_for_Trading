import pandas as pd
import numpy as np
import scipy.stats as stats

# Get returns, volatility



close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],},
    pd.date_range('10/01/2018', periods=5, freq='D'))

close.shift(2)

def calculate_returns(close):
    """
    Compute returns for each ticker and date in close.

    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """
    shifted = close.shift(1)
    #     print(close)
    #     print((close - shifted))
    #     print((close - shifted)/shifted)

    return (close - shifted) / shifted


def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    # TODO: Perform one-tailed t-test on net_returns
    # Hint: You can use stats.ttest_1samp() to perform the test.
    #       However, this performs a two-tailed t-test.
    #       You'll need to divde the p-value by 2 to get the results of a one-tailed p-value.
    # ref: https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
    null_hypothesis = 0.0
    t, p = stats.ttest_1samp(net_returns, null_hypothesis)
    return t, p / 2


def test_run(filename='net_returns.csv'):
    """Test run analyze_returns() with net strategy returns from a file."""
    net_returns = pd.Series.from_csv(filename, header=0)
    t, p = analyze_returns(net_returns)
    print("t-statistic: {:.3f}\np-value: {:.6f}".format(t, p))


def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    max_std = 2  # Range is 0.1-0.5
    max_tick = ''
    # TODO: Fill in this function.
    for tic in prices['ticker'].unique():
        print(tic)
        curr_std = get_volatility(prices[prices['ticker'] == tic])
        if max_tick == '':
            max_tick = tic
            max_std = curr_std
        if max_std < curr_std:
            max_tick = tic
            max_std = curr_std
    return max_tick


def get_volatility(df):
    # Calculate log returns
    lret = np.log(df['price']) - np.log(df['price'].shift(1))
    lret_std = lret.std()
    return lret_std


def estimate_volatility(prices, l):
    """
    https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html#exponentially-weighted-windows
    Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.

    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.

    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less
        relative to more recent terms.

    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.

    """
    # TODO: Implement the exponential moving average volatility model and return the last value.
    lret = np.log(prices) - np.log(prices.shift(1))
    lret = lret ** 2
    lret = lret.ewm(alpha=1 - l).mean()
    res = pow(lret, 0.5)
    print(res.values[-1])
    return res.values[-1]


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))

    prices = pd.read_csv(filename, parse_dates=['date'], index_col='date', squeeze=True)
    print("Most recent volatility estimate: {:.6f}".format(estimate_volatility(prices, 0.7)))


if __name__ == '__main__':
    test_run()