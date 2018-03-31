import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''' read file '''
data = pd.read_csv("105Jongli_and_Taoyuan.csv", encoding="big5")

#data_clean1 = data[data['PM2.5']>0]                                        # clean the data
data_clean1 = data[data['PM10']>0]
x1 = data_clean1.loc[:,'PM2.5']                           
y1 = data_clean1.loc[:,'PM10']


''' regression line '''
mx = x1.mean()
my = y1.mean()
temp = x1 - mx
c1 = np.sum(temp*(y1 - my) / np.sum(temp ** 2))
c0 = my - c1 * mx

X1 = [0,x1.count()]
Y1 = [c0 + c1*0 , c0 + c1*x1.count()]

print(round(c0,2))
print(round(c1,2))

''' draw '''
plt.scatter(x1, y1, s=2)
plt.xlabel("PM2.5")
plt.ylabel("PM10")
plt.title("PM10_PM2.5_correlation")
plt.plot(X1, Y1, color='r')                                                 # regression line
plt.text(40, 40, 'PM10 = %s + %s*PM2.5'%(round(c0,2),round(c1,2)),         # formula
    color='r', size=16)       
plt.axis([0,120,0,250])
plt.show()

x1.to_csv("test.csv", encoding="big5")