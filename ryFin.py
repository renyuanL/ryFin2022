import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import yfinance as yf

def getTicker(tkName='^GSPC'):
    #tkName= 'QQQ'
    tk= yf.Ticker(tkName)
    df= tk.history(period='max')
    df= df[['Open','High','Low','Close']].mean(axis=1)
    df.name= tkName
    df.to_csv(f'{tkName}.csv')
    return df

X= getTicker()



def getGains(tkName= '^GSPC', afterDays= list(range(0,1001,100))):
    #tkName= 'QQQ'
    df= getTicker(tkName)
    gainL= []
    #columns= list(range(0,20,1))
    for n in afterDays:
        gain= df.shift(-n)/df
        gainL += [gain]
    gainL= pd.DataFrame(gainL).transpose()
    gainL.columns= afterDays
    gainL.name= tkName
    gainL.describe()
    return gainL

Y= getGains()
