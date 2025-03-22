# IN PROGRESS
def Binomial_Tree_Eur(S0,K,r,T,N,IV,type):

    import numpy as np
    import math as m

## Parameters
    dT = T/N
    discount_fac = m.exp(-r*T)
    up = m.exp(IV * np.sqrt(dT))
    down  = m.exp(-IV * np.sqrt(dT))
    p = (m.exp(r * dT) - down) / (up - down)

    
## Calculating value at each end of tree, N+1 branches
    values = np.zeros(N+1)
    probs = np.zeros(N+1)
    EV = 0

    for ind,val in enumerate(values):
        probs[ind] = m.factorial(N)/(m.factorial(ind)*m.factorial(N-ind)) * p**(N-ind) * (1-p)**(ind)
        if type == 'call':
            values[ind] = max(S0 * up**(N-ind) * down**(ind) - K,0)
        elif type == 'put':
            values[ind] = max(K - S0 * up**(N-ind) * down**(ind),0)
        EV += values[ind] * probs[ind]

    EVdisc = EV * discount_fac

    val = round(EVdisc,2)

    return val

# IN PROGRESS
def Black_Scholes_Pricing(S0,K,r,xpiry,IV,type):

    import datetime
    import numpy as np
    from scipy.stats import norm

    # time to expiry as an int
    today = datetime.date.today()
    expiry = np.datetime64(xpiry)
    ttxp = np.busday_count(today,expiry)

    w = (np.log(S0/K) + (r + .5 * IV**2) * ttxp)/(np.sqrt(ttxp) * IV)

    if type == 'call':
        C = S0 * norm.cdf(w,loc = 0,scale = 1) - np.exp(-r*ttxp)*K*norm.cdf(w - IV*ttxp,loc = 0,scale = 1)
        return C
    elif type == 'put':
        P = np.exp(-r*ttxp) * K * norm.cdf(-w + IV * ttxp,loc = 0,scale = 1) - S0 * norm.cdf(-w,loc = 0,scale = 1)
        return P 

# Working to integrate with BS
def IV_solver(S0,K,r,xpiry,type,MKT_price):
    
    import scipy.optimize as opt
    
    objective = lambda IV: Black_Scholes_Pricing(S0,K,r,xpiry,IV,type) - MKT_price
    sol = opt.brentq(objective)
    
    return sol

# my functions seem to be overshooting the value, why is this? Theoretical, or incorrect implementation?
