from APIcustomerloan import customerloan
import tensorflow, pandas, numpy
from keras.api.models import Sequential
from keras.api.layers import Dense, Dropout, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from statsmodels import api

predictors_col = customerloan.drop(columns=["approval_date", "loan_amount"])
target_col = customerloan["loan_amount"]

X_train, X_test, y_train, y_test = train_test_split(predictors_col, target_col, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
