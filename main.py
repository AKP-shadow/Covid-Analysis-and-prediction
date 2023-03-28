import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import  linear_model, metrics

    
df = pd.read_csv("covid_19_india.csv")
print(df.columns)
state_colors={}
deathTable ={}
recoveredTable={}
for case in range(35):
    state = df.iloc[-case]['State/UnionTerritory'].strip("*")
    deathTable[state]=int(df.iloc[-case]['Deaths'])
    recoveredTable[state]=int(df.iloc[-case]['Cured'])
    state_colors[state] = list(np.random.choice(range(255),size=3))
    
# print(deathTable)    
# print(list(deathTable.keys()))
    
plt.style.use('ggplot')
plt.title("State vs Death")
plt.barh(list(deathTable.keys()),list(deathTable.values()))
plt.xlabel("Deaths")
plt.ylabel("States")
plt.show()

plt.style.use('ggplot')
plt.title("State vs Recovered")

plt.barh(list(recoveredTable.keys()),list(recoveredTable.values()))
plt.xlabel("Recovered")
plt.ylabel("States")
plt.show()


x_train=np.array(df["Cured"])
y_train=df["Deaths"]
reg = linear_model.LinearRegression()
print(x_train.shape)
print(y_train.shape)
x_train = x_train.reshape(-1,1)
reg.fit(x_train,y_train)
print(reg.coef_)
plt.scatter(df["Cured"],df["Deaths"])
plt.xlabel("Recovered")
plt.ylabel("Deaths")
plt.title("Linear Regression Model to predict death per recovered")
plt.plot(np.array(df['Cured']),reg.coef_*df['Cured'],color="yellow")
plt.show()
