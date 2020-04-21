import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileNmIn='Data.xlsx'

df=pd.read_excel('Data.xlsx',sheet_name='Sheet1')
N=df.shape[0]
xSum=df['x'].sum()
ySum=df['y'].sum()

xSumSquare=xSum**2
xSquareSum=df['x'].pow(2).sum()
df['x*y']=df['x']*df['y']
xySum=df['x*y'].sum()

m=(N*xySum-xSum*ySum)/(N*xSquareSum-(xSum*xSum))
b=(ySum-m*xSum)/N

(x3,y3)=(4.5,11)
error3=np.abs(y3-(x3*m+b))

(x5,y5)=(6.6, 16.4)
error5=np.abs(y5-(x5*m+b))


print('m=%.2f b=%.2f e3=%.2f e5=%.2f'%(m,b,error3,error5))

x1=np.array(df['x'])
y1=np.array(df['y'])
m1,b1=np.polyfit(x1,y1,1)
plt.plot(x1,y1,'o')
plt.plot(x1,m1*x1+b1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
