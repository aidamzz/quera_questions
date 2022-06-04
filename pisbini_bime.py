import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, roc_auc_score, accuracy_score

train = pd.read_csv("../data/travel_insurance/train.csv")
test = pd.read_csv("../data/travel_insurance/test.csv")
train = train.drop("Customer Id", axis=1)
catCols = ["Employment Type", "GraduateOrNot", "ChronicDiseases", "FrequentFlyer", "EverTravelledAbroad"]
numCols = ["Age", "AnnualIncome", "FamilyMembers"]
train = pd.get_dummies(train, columns=catCols)
y_train = train['TravelInsurance'].replace({"No": 0, "Yes": 1})
X_train = train.drop("TravelInsurance", axis=1)
mmSc = MinMaxScaler()
mmSc.fit(X_train[numCols])
X_train
extra = pd.DataFrame(mmSc.transform(X_train[numCols]), columns=numCols)
X_train = X_train.drop(numCols, axis=1).join(extra)
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train)
