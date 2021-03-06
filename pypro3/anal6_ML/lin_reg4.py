# iris dataset으로 선형회귀분석
# 상관관계가 약한 경우와 강한 경우로 분석 모델을 작성해 비교

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

iris = sns.load_dataset('iris')
print(iris.head(3), iris.shape)
print(iris.corr(method='pearson'))

# 단순 선형회귀
# 1. 상관관계가 약한 두 변수
result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()
print('요약결과1:', result1.summary())
print('R squared:',result1.rsquared)
print('p values:',result1.pvalues[1])
#  모델은 의미 없는 모델이다.
print('실제 값 :', iris.sepal_length[:5].values)
print('예측 값 :', result1.predict()[:5])

print('--------------------------')
# 2. 상관관계가 강한 두 변수
result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()
print('요약결과2:', result2.summary())
print('R squared:',result2.rsquared) #R squared: 0.7599546457725151
print('p values:',result2.pvalues[1]) # p values: 1.0386674194500194e-47 < 0.05
#  모델은 의미 없는 모델이다.
print('실제 값 :', iris.sepal_length[:5].values)
print('예측 값 :', result1.predict()[:5])

# 새로운 값(petal_length)으로 미지의 sepal_length 값 얻기
new_data = pd.DataFrame({'petal_length':[1.1, 0.5, 5.0]})
y_pred = result2.predict(new_data)
print('예측 결과:', y_pred.values)

print('--------------------------')
# 다중 선형회귀 : 독립변수 복수
# result3 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width + sepal_width',data=iris).fit()
# print('요약 결과3:',result3.summary())

# 여러개의 독립변수는 join을 사용한다.
column_select = "+".join(iris.columns.difference(['sepal_length','species']))
print(column_select)
result3 = smf.ols(formula = 'sepal_length ~' + column_select ,data=iris).fit()
print('요약 결과4:',result3.summary())