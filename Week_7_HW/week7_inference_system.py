# -*- coding: utf-8 -*-
"""ML_APP_Week7_inference_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YxJOZX1yR5kBkY7BBFQwOsPM6F7tpVuf
"""

# from google.colab import files
import tensorflow as tf
# files.upload()
model = tf.keras.models.load_model('week_7_model_ROC_88.h5')

import pandas as pd
# files.upload()
#unzipping the zip file - got code from https://www.geeksforgeeks.org/unzipping-files-in-python/ 

# importing the zipfile module
from zipfile import ZipFile
  
# loading the temp.zip and creating a zip object
with ZipFile("Week_7_HW/IS_x_test_df.csv.zip", 'r') as zObject:
  
    # Extracting specific file in the zip
    # into a specific location.
    zObject.extract(
        "IS_x_test_df.csv", path="Week_7_HW")
zObject.close()

with ZipFile("Week_7_HW/IS_y_test_df.csv.zip", 'r') as zObject:
  
    # Extracting specific file in the zip
    # into a specific location.
    zObject.extract(
        "IS_y_test_df.csv", path="Week_7_HW")
zObject.close()


X = pd.read_csv('IS_x_test_df.csv')
Y = pd.read_csv('IS_y_test_df.csv')

corrs = ['card3','D2','D7','D8','D15','V15','V16','V17','V18','V21','V22','V23','V24','V29','V30','V31','V32','V33','V34','V35','V37','V38','V39','V40','V42','V43','V44','V45','V46','V47','V48','V49','V50','V51','V52','V57','V58','V59','V60','V63','V64','V67','V69','V70','V71','V72','V73','V74','V77','V78','V79','V80','V81','V84','V85','V86','V87','V90','V91','V92','V93','V94','V108','V110','V111','V112','V113','V114','V116','V123','V124','V125','V139','V140','V141','V142','V146','V147','V148','V149','V153','V154','V155','V156','V157','V158','V170','V171','V176','V184','V185','V186','V188','V189','V190','V194','V195','V197','V198','V199','V200','V201','V220','V221','V222','V228','V229','V230','V235','V238','V239','V242','V243','V244','V245','V246','V247','V248','V249','V252','V257','V258','V259','V260','V261','V262','V282','V283','V302','V303','V304','TransactionID','TransactionDT','TransactionAmt','ProductCD','card1','card2','card4','card5','card6','addr1','addr2','dist1','P_emaildomain','R_emaildomain']

cols = corrs.copy()
for i in ['ProductCD', 'card4', 'card6', 'P_emaildomain', 'R_emaildomain']:
  cols.remove(i)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

#normalize - code from dave's colab
x_norm_df = X[corrs] #using the columns from the top
x_norm_df.TransactionAmt = (x_norm_df.TransactionAmt - X.TransactionAmt.mean()) / X.TransactionAmt.std()
#One hot code
x_oh_df = pd.get_dummies(x_norm_df)
# for i in cols:
#   print(i)
x_oh_df = x_oh_df[cols]

x_oh_df = x_oh_df.fillna(-1.5)


x_oh_df_scaled = x_oh_df.copy()
# apply scaler techniques
x_oh_df_scaled = scaler.fit_transform(x_oh_df_scaled)
print(x_oh_df_scaled)

x_oh_df

pred = model.predict(x_oh_df_scaled)

import numpy as np
temp = []
for i in np.round(pred.copy()):
  temp.append(int(i))

Y = Y['isFraud']

from sklearn.metrics import classification_report
rounded = temp
print(classification_report(Y, temp))

from sklearn.metrics import roc_auc_score
print("ROC SCORE IS: " + str(roc_auc_score(Y, pred)))