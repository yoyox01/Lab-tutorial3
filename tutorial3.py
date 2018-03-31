import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''' read file '''
data = pd.read_csv("105Jongli_and_Taoyuan.csv", encoding="big5")

#data_clean1 = data[data['PM2.5']>0]                                        # clean the data
data_clean1 = data[data['PM10']>0]
x1 = data_clean1.loc[:,'PM2.5']                           
y1 = data_clean1.loc[:,'PM10']



''' (1) '''
''' regression line '''
mx = x1.mean()
my = y1.mean()
temp = x1 - mx
c1 = np.sum(temp*(y1 - my) / np.sum(temp ** 2))
c0 = my - c1 * mx

X1 = [0,x1.count()]
Y1 = [c0 + c1*0 , c0 + c1*x1.count()]



''' draw '''
plt.scatter(x1, y1, s=2)
plt.plot(X1, Y1, color='r')                                                 # regression line
plt.text(40, 40, 'PM10 = %s + %s*PM2.5'%(round(c0,2),round(c1,2)),          
    color='r', size=16)                                                     # formula
plt.axis([0,120,0,250])
plt.xlabel("PM2.5")
plt.ylabel("PM10")
plt.title("PM10_PM2.5_correlation")
plt.show()



''' (2) '''
data_clean2 = data.loc[:,['date','location','PM2.5',]]                     # data clean
data_clean2_J = data_clean2.loc[data_clean2.location==u'中壢']
data_clean2_T = data_clean2.loc[data_clean2.location==u'桃園']
data_clean2_J = data_clean2_J.groupby('date').mean()                       # group by date
data_clean2_T = data_clean2_T.groupby('date').mean()

x2 = data_clean2_J.index
y2_J = data_clean2_J.loc[:,'PM2.5']
y2_T = data_clean2_T.loc[:,'PM2.5']

plt.scatter(x2, y2_J, s=4, label="Jongli", marker='^', color='r')
plt.scatter(x2, y2_T, s=4, label="Taoyuan")
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.title("2016_PM2.5_aggregate_by_date")
plt.legend()
plt.show()



''' (3) '''
data_clean3 = data.loc[:,['time','location','PM2.5',]]                     # data clean
data_clean3_J = data_clean3.loc[data_clean2.location==u'中壢']
data_clean3_T = data_clean3.loc[data_clean2.location==u'桃園']
data_clean3_J = data_clean3_J.groupby('time').mean()                       # group by date
data_clean3_T = data_clean3_T.groupby('time').mean()

x3 = data_clean3_J.index
y3_J = data_clean3_J.loc[:,'PM2.5']
y3_T = data_clean3_T.loc[:,'PM2.5']

plt.plot(x3, y3_J, '--o', label="Jongli", color='r', marker='^')
plt.plot(x3, y3_T, '--o', label="Taoyuan")
plt.xlabel("Time")
plt.ylabel("PM2.5")
plt.title("2016_PM2.5_aggregate_by_time")
plt.legend()
plt.show()
#data_clean3_J.to_csv("test.csv", encoding="big5")