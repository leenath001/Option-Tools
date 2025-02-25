def Binomial_Tree_Eur(S0,K,r,T,N,IV,ticker,type):

    import Param_Est
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

    return val,sig,p




    
    
    
