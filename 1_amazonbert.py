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
PTH = os.environ.get('PTH')

# load the CSV file "Category.csv" with texts labels
df = pd.read_csv(os.path.join(PTH,"Category.csv"))

# choose between: [Service, Varies, Interaction, Technical, No specified failures]
term = 'No specified failures'

df = df[['id','text',term]] # <id, text, label>

# Creating train and dev dataframes according to BERT
df_bert = pd.DataFrame({'index_col':df['id'],
            'label':le.fit_transform(df['label']),
            'alpha':['a']*df.shape[0],
            'text':df['text'].replace(r'\n',' ',regex=True)})

# split into Training and Testing sets (set the size of the split)
df_bert_train, df_test = train_test_split(df_bert, test_size=0.3)

# split into Train and Validation sets (set the size of the split)
df_bert_train, df_bert_dev = train_test_split(df_bert_train, test_size=0.1)

# Creating test dataframe according to BERT
df_bert_test = pd.DataFrame({'index_col':df_test['index_col'],
                 'text':df_test['text'].replace(r'\n',' ',regex=True)})

# Saving dataframes to .tsv format as required by BERT
df_bert_train.to_csv('./bert/data/train.tsv', sep='\t', index=False, header=False)
df_bert_test.to_csv('./bert/data/test.tsv', sep='\t', index=False, header=True)
df.to_csv('./bert/data/full_data.csv', sep=',', index=False, header=True)
df_bert_dev.to_csv('./bert/data/dev.tsv', sep='\t', index=False, header=False)
