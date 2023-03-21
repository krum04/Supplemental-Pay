# datereturns.py
import pandas as pd
from datetime import date, timedelta

def dates_return():
    """
    Returns a dictionary of the current pay period and the dates in that pay period
    """
    
    payperiod = pd.read_csv('payperiod.csv')
    payperiod['pay_date']= pd.to_datetime(payperiod['pay_date'])
    payperiod['starting']= pd.to_datetime(payperiod['starting'])
    payperiod['ending']= pd.to_datetime(payperiod['ending'])
    payperiod['due']= pd.to_datetime(payperiod['due'])
  
    curDate = date.today()
    
    payPeriodDict = {}
    for _, row in payperiod.iterrows():
        start = row['starting']
        startDue = row['starting'] + timedelta(days=4)
        end = row['ending']
        due = row['due']
        if startDue <= curDate <= due:
            payPeriodDict['Period'] = row['period']
            payPeriodDict['Due'] = row['due'].strftime('%m/%d/%y')
            payPeriodDict['Dates'] = []
            delta = end - start
            count = 1
            for i in range(delta.days + 1):
                day = row['starting'] + timedelta(days=i)
                payPeriodDict['Dates'].append(day.strftime('%m/%d/%y'))
                count += 1
            
    return payPeriodDict