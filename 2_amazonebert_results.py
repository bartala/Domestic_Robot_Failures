from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pandas import DataFrame
le = LabelEncoder()
import pandas as pd
import os
import requests
from dotenv import load_dotenv
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

load_dotenv(verbose=True)

# define variables
PTH_A = os.environ.get('PTH_to_classifications')
PTH= os.environ.get('PTH')

df_results = pd.read_csv(os.join.path(PTH_A,"bert_output.tsv"),sep="\t",header=None)
df_test = pd.read_csv(os.join.path(PTH,"bert/data/test.tsv"),sep="\t",header=None)

df_results_csv = pd.DataFrame({'index_col':df_test['index_col'].tolist(),
                               'Is_Response':df_results.idxmax(axis=1)})
                               
x = pd.merge(df_test, df_results_csv, on='index_col')

# print the confusion matrix
y_test = x['label'].tolist()
y_pred = x['Is_Response'].tolist()
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
