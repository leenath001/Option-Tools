# Option-Tools

## Binomial_Tree_Eur(S0,K,r,T,N,IV,type):
Binomial Tree model used to price european options
*  S0 : Initial price
*  K : Strike
*  r : risk-free rate
*  T : days till expiry
*  N : number of branches (end node has N+1 possibilities)
*  IV : Implied volatility
*  type : 'call' or 'put'

## opt_data(ticker,type)
Utilizes yfinance API to grab option chain data. Provides strikes, last price, and IV data. Function asks user for desired expiry date to provide relevant chain.
*  ticker : takes str input. (i.e 'AAPL')
*  type : 'call' or 'put'

## equity_data(ticker,start,end)
Utilizes yfinance API to grab equity data. Provides open, close, high, low, and volume data. 
*  ticker : takes str input. (i.e 'AAPL')
*  start : start date of desired data (inclusive)
*  end : end date of desired data (exclusive) 

Currently working on a volatility space constructor 
