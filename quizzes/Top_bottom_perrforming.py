import pandas as pd
import datetime

month = pd.to_datetime('02/01/2018')
stock_series = pd.DataFrame(
    {
        'A': 1,
        'B': 12,
        'C': 35,
        'D': 3,
        'E': 79,
        'F': 2,
        'G': 15,
        'H': 59},
    [month])

stock_series


def get_top_performing(stock_series, n=2):
    # try: not df func
    #     # Attempt to run nlargest
    #     close_month.nlargest(2)
    # except TypeError as err:
    #     print('Error: {}'.format(err))

    ## Series.nlargest(2)
    return stock_series.loc[month].nlargest(n)


def get_lowest_performing(stock_series, n=2):
    # Can user stock_series.nsmallest(2)
    return (-1 * stock_series).loc[month].nlargest(n) * -1
