import datetime as dt
import pandas_datareader as pdr   # remote access data reader
import matplotlib as style
import matplotlib.pyplot as plt

def requirements():
    print('''1. Run demo.py
2. If errors, more than likely missing installations.
3. Test Python Package installer: pip freeze
4. Research how to do the following installations:
    a. pandas
    b. padas-datareader
    c. matplotlib
5. Create at least three functions''')

def data_analysis():
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()

    # read data into Pandas dataframe
    df = pdr.DataReader('XOM', 'yahoo', start, end) #remote data access

# convert to pandas module from DataReader
    #df1 = pd.DataFrame.from_records(df) #put information into a pandas DataFrame
    print("Print number of records")
    print(df.shape[0])
    print()

    print("print columns")
    print(df.columns)
    print()

    print("Print dataframe")
    print(df[0:60])
    print(df.shape)
    print()

    print('Print first 5 lines')
    print(df[0:5])
    print()

    print('Print last 5 lines')
    print(df[-6:-1])
    print()

    print('Print first 2 lines')
    print(df[0:2])
    print()

    print('Print last 2 lines')
    print(df[-3:-1])

    #Plot using matplotlib.pyplot class
    plt.style.use('ggplot')
    df['High'].plot()
    df['Adj Close'].plot()
    plt.legend()
    plt.show()

def main():
    requirements()
    data_analysis()

if __name__ == "__main__":
   main()