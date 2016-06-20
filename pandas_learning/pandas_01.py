import pandas as pd
import numpy as np


# Series Type
def test_01():
    S = pd.Series([3, 6, 9])
    print(S)
    print(S.index)
    print(S.values)
    print(type(S.values))  # numpy.ndarray

    #  create an individual index instead of the default index
    fruits = ['apples', 'oranges', 'cherries', 'pears']
    quantities = [20, 33, 52, 10]
    S = pd.Series(quantities, index=fruits)
    print(S)
    print(S['apples'])
    print(S[['apples', 'oranges']])  # <class 'pandas.core.series.Series'>


def test_02():
    quantities = [20, 33, 52, 10]
    S = pd.Series(quantities, index=['apples', 'oranges', 'cherries', 'pears'])
    # Filtering with a boolean array
    print(S[S > 20])

    cities = {"London": 8615246,
              "Berlin": 3562166,
              "Madrid": 3165235,
              "Rome": 2874038,
              "Paris": 2273305,
              "Vienna": None}
    city_series = pd.Series(cities)
    print(city_series)
    print(city_series.isnull())


def test_03():
    """
    DataFrame Type: spreadsheet-like
        It contains an ordered collection of columns. Each column consists of a unique data type,
        but different columns can have different types
    """
    cities = {
        "name": ["London", "Berlin", "Madrid", "Rome",
                 "Paris", "Vienna", "Bucharest", "Hamburg",
                 "Budapest", "Warsaw", "Barcelona",
                 "Munich", "Milan"],
        "population": [8615246, 3562166, 3165235, 2874038,
                       2273305, 1805681, 1803425, 1760433,
                       1754000, 1740119, 1602386, 1493900,
                       1350680],
        "country": ["England", "Germany", "Spain", "Italy",
                    "France", "Austria", "Romania",
                    "Germany", "Hungary", "Poland", "Spain",
                    "Germany", "Italy"],
        "area": [1572, 891.85, 605.77, 1285,
                 105.4, 414.6, 228, 755,
                 525.2, 517, 101.9, 310.4, 181.8]
    }
    city_frame = pd.DataFrame(cities, columns=["country", "name", "population", "area"], )
    print(city_frame)

    # print(city_frame['population'].sum())
    # print(city_frame['population'].cumsum())

    print(type(city_frame['population']))  # <class 'pandas.core.series.Series'>
    # Access a column of the DataFrame
    # print(city_frame['population'])
    # print(city_frame.population)

    # Access the rows of the DataFrame
    # print(city_frame.ix[0])

    # Sort the DataFrame
    city_frame = city_frame.sort_values(by='area', ascending=False)
    print(city_frame)


def test_04():
    """
    A nested dictionary of dicts can be passed to a DataFrame as well.
    The indices of the outer dictionary are taken as the the columns and the inner keys. i.e.
    the keys of the nested dictionaries, are used as the row indices:
    """
    growth = {"Switzerland": {"2010": 3.0, "2011": 1.8, "2012": 1.1, "2013": 1.9},
              "Germany": {"2010": 4.1, "2011": 3.6, "2012": 0.4, "2013": 0.1},
              "France": {"2010": 2.0, "2011": 2.1, "2012": 0.3, "2013": 0.3},
              "Greece": {"2010": -5.4, "2011": -8.9, "2012": -6.6, "2013": -3.3},
              "Italy": {"2010": 1.7, "2011": 0.6, "2012": -2.3, "2013": -1.9}
              }
    growth_frame = pd.DataFrame(growth)
    # growth_frame = growth_frame.reindex(["2013", "2012", "2011", "2010"])
    print(growth_frame)
    # Transpose the data
    print(growth_frame.T)


def test_05():
    # Filling a DataFrame with random data
    df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
    # print(df)

    # Read in a csv file
    score_frame = pd.read_csv("country.csv", quotechar="'", sep=",", thousands=",", encoding="utf-8")
    print(score_frame)


if __name__ == '__main__':
    # test_01()
    # test_02()
    # test_03()
    # test_04()
    test_05()
