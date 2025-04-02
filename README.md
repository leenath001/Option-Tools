# Option-Tools

## Binomial_Tree_Eur(S0,K,r,T,N,IV,type):
Binomial Tree model used to price european options (Currently troubleshooting. Affects IV_solver fun)
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

## equity_bidask(ticker)
Provides bid/ask price of specified security. Outputs bidask [0], bid [1], and ask [2]

## opt_data_IVchain(ticker)
Provides option data for OTM puts/calls. Pandas DF is arranged as follows [OTM puts, OTM calls]. Use case is for plotting vol smile/3d vol surface
*  OTM options are used as they are more actively traded, providing accurate data.
*  Vol smile implies expected upwards/downside movement by traders. OTM calls/puts are used to hedge.
*  Vol smirk implies expeced downside movement by traders. OTM puts are used to hedge 
See main for plotting of vol smile/smirk example

## IV_solver(S0,K,r,T,N,type,MKT_price,IV_guess)
Uses Binomial_Tree_Eur and scipy to solve for IV. 
*  S0 : Initial price
*  K : Strike
*  r : risk-free rate
*  T : days till expiry
*  N : number of branches (end node has N+1 possibilities)
*  IV : Implied volatility
*  type : 'call' or 'put'
*  MKT_price : current traded price of option
*  IV_guess : guess to initialize function. 
Currently working on a volatility space constructor 

## Put_Call_ratio(ticker)
*  Returns ratio of puts/calls traded on most active contracts
*  Uses first OTM put and call volume to calculate ratio
*  Ratio > 1 implies expected bearish move -> traders buying more puts than calls
*  Ratio < 1 implies expected bullish move -> traders buying more calls than puts
