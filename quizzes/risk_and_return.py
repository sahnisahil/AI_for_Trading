import numpy as np


def covariance_matrix(returns):
    """
    Create a function that takes the return series of a set of stocks
    and calculates the covariance matrix.

    Parameters
    ----------
    returns : numpy.ndarray
        2D array containing stock return series in each row.

    Returns
    -------
    x : np.ndarray
        A numpy ndarray containing the covariance matrix
    """

    # covariance matrix of returns
    cov = np.cov(returns)

    return cov


# quiz_tests.test_covariance_matrix(covariance_matrix)

"""Test with a 3 simulated stock return series"""
days_per_year = 252
years = 3
total_days = days_per_year * years

return_market = np.random.normal(loc=0.05, scale=0.3, size=days_per_year)
return_1 = np.random.uniform(low=-0.000001, high=.000001, size=days_per_year) + return_market
return_2 = np.random.uniform(low=-0.000001, high=.000001, size=days_per_year) + return_market
return_3 = np.random.uniform(low=-0.000001, high=.000001, size=days_per_year) + return_market
returns = np.array([return_1, return_2, return_3])

"""try out your function"""
cov = covariance_matrix(returns)

print(f"The covariance matrix is \n{cov}")