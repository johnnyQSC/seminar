import pandas as pd
from xgboost.sklearn import XGBClassifier,XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
import time
from sklearn.metrics import mean_absolute_error,mean_squared_error,mean_absolute_percentage_error
df=pd.read_csv("106-109_TrainingDatasets.csv") # 資料讀取
x= df.loc[:,['光線代碼', '道路第1當事者_代碼', '道路型態子類別代碼','事故位置子類別代碼',
       '車道劃分設施_分向設施大類別代碼', '車道劃分設施_分向設施子類別代碼',
       '車道劃分設施_快慢車道間代碼', '事故類型及型態大類別代碼',
       '肇因研判大類別代碼_主要', '肇因研判大類別代碼_個別']] # x為特徵值
y= df.loc[:,['車道劃分設施_快車道或一般車道間代碼']] # y為預測目標
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #將資料集分成訓練資料(80%)及與測試資料集(20%)
#XGBoost
print("XGBoost")
start=time.time()
xgb_clf=XGBClassifier(eta=0.01,max_depth=30,subsample=0.5)
xgb_clf.fit(x_train,y_train)
y_prediction=xgb_clf.predict(x_test)
end=time.time()
print("XGBoost 訓練準確率: ",xgb_clf.score(x_train,y_train))
print("XGBoost 測試準確率: ",xgb_clf.score(x_test,y_test))
print("運算時間: ",end-start)
print("--------------------------------------------------")
print("XGBoost 分類結果報告")
print(classification_report(y_test,y_prediction))
print("XGBoost 混淆矩陣")
print(confusion_matrix(y_test,y_prediction))
print("MAE: ",mean_absolute_error(y_test,y_prediction))
print("RMSE: ",mean_squared_error(y_test,y_prediction))
print("MAPE: ",mean_absolute_percentage_error(y_test,y_prediction))
print("--------------------------------------------------")