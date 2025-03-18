import yfinance as yf
import pandas as pd
import numpy as np
import Data_Funcs as df
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

def opt_data_IVchain(ticker):
    stoxx = yf.Ticker(ticker)
    expirations = stoxx.options

    # Grabbing current fair price of underlying
    ba = df.equity_bidask(ticker)
    S = (ba[1] + ba[2]) / 2 

    vol_surface_data = []

    for expiry in expirations:
        option_chain = stoxx.option_chain(expiry)
        calls = option_chain.calls[['strike', 'impliedVolatility']]
        puts = option_chain.puts[['strike', 'impliedVolatility']]

        # Adjust strike relative to spot price
        putstrikesadj = puts['strike'] - S
        callstrikesadj = calls['strike'] - S

        # Find OTM puts and calls
        def find_first_positive(column):
            positive_values = column[column > 0]
            if not positive_values.empty:
                return positive_values.index[0]

        x = find_first_positive(callstrikesadj)
        y = find_first_positive(putstrikesadj) - 1

        volframeputs = puts.loc[0:y, :]
        volframecalls = calls.loc[x:, :]
        MASVF = volframeputs._append(volframecalls)
        MASVF.index = range(len(MASVF))

        # Store strike, IV, and expiration in days
        for _, row in MASVF.iterrows():
            vol_surface_data.append([row['strike'], row['impliedVolatility'], expiry])

    return pd.DataFrame(vol_surface_data, columns=['Strike', 'IV', 'Expiration'])

def plot_vol_curve(ticker):
    x = df.opt_data_IVchain(ticker)
    S1 = df.equity_bidask(ticker)
    S = (S1[1] + S1[2])/2

    X = x.loc[:,'strike']
    Y = x.loc[:,'impliedVolatility']

    plt.plot(X,Y)
    plt.xlabel('Strikes')
    plt.ylabel('IV')
    plt.title("Ticker : {}, Current Price : {}".format(ticker,S))
    plt.show()

def plot_vol_surface(ticker):
    vol_data = opt_data_IVchain(ticker)

    today = pd.Timestamp.today()
    vol_data['Expiration'] = vol_data['Expiration'].apply(lambda x: (pd.Timestamp(x) - today).days)

    X = vol_data['Strike'].values
    Y = vol_data['Expiration'].values
    Z = vol_data['IV'].values

    strike_grid = np.linspace(X.min(), X.max(), 50)  
    expiry_grid = np.linspace(Y.min(), Y.max(), 50)  
    X_grid, Y_grid = np.meshgrid(strike_grid, expiry_grid)

    Z_grid = griddata((X, Y), Z, (X_grid, Y_grid), method='cubic')

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X_grid, Y_grid, Z_grid, cmap='jet', edgecolor='none')

    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Days to Expiry')
    ax.set_zlabel('Implied Volatility')
    ax.set_title(f'Implied Volatility Surface for {ticker}')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


