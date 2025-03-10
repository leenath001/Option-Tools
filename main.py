
import Data_Funcs as of
import pandas as pd
import matplotlib.pyplot as plt

dat = of.opt_data_IVchain('SPY')
print(dat)

x = dat.loc[:,'strike']
y = dat.loc[:,'impliedVolatility']

plt.plot(x,y)
plt.show()