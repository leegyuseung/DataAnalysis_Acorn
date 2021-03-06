# sklearn 모듈의 분류 모델의 상당수는 출력결과가 연속형인 예측 처리도 가능

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

boston = load_boston()

dfx = pd.DataFrame(boston.data, columns = boston.feature_names)
dfy = pd.DataFrame(boston.target, columns = ['MEDV'])
df = pd.concat([dfx, dfy], axis = 1)
print(df.head(3),df.shape) #(506,14)

print(df.corr())

cols = ['MEDV', 'RM', 'LSTAT']
# sns.pairplot(df[cols])
# plt.show()

x = df[['LSTAT']]
y = df['MEDV']

# 실습 1 : DecisionTreeRegressor
model = DecisionTreeRegressor (criterion = 'mse').fit(x,y)
print('predict:',model.predict(x)[:5])
print('real:', np.array(y[:5]))
print('결정계수(R2):',r2_score(y, model.predict(x)))

print('---------------------')
# 실습 2 : RandomForestRegressor
model = RandomForestRegressor(n_estimators = 1000, criterion = 'mse', random_state = 123).fit(x,y)
print('predict:',model.predict(x)[:5])
print('real:', np.array(y[:5]))
print('결정계수(R2):',r2_score(y, model.predict(x)))