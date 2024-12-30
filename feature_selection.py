from APIcustomerloan import customerloan
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from statsmodels import api

predictors_col = customerloan.drop(columns=["approval_date", "loan_amount"])
target_col = customerloan["loan_amount"]

# feature selection
# Ordinary Least Squares - the technique for fitting a linear regression model by minimizing the sum of squared residuals (errors)
# Ordinary Least Squares - used in regression analysis to estimate the parameters of a linear model. Its goal is to minimize the differences between observed values and predicted values (i.e., residuals).

X_tr, X_ts, y_tr, y_ts = train_test_split(predictors_col, target_col, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_tr, y_tr)
X_tr_const = api.add_constant(X_tr)
model_OLS = api.OLS(y_tr, X_tr_const).fit()
# print(model_OLS.summary()) # feature_selection



