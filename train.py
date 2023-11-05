import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('train.csv')

categorical = ['hearing(left)', 'hearing(right)', 'dental caries']
numerical = list(set(df.columns) - set(categorical) - {'id'})
df[categorical] = df[categorical].astype(str)

df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.smoking.values
y_test = df_test.smoking.values

del df_train['smoking']
del df_test['smoking']

del df_train['id']
del df_test['id']

dv = DictVectorizer(sparse=False)
train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)


from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_curve, roc_auc_score

# Create a pipeline with MinMaxScaler and XGBoost
pipeline = Pipeline([
    ('scaler', MinMaxScaler()),
    ('xgb', XGBClassifier(learning_rate=0.1, max_depth=5, n_estimators=300))
])

# Fit the pipeline to your training data
print("Training the model ...")
print("Waite for a moment")
pipeline.fit(X_train, y_train)
print("Training finished")

# Predict probabilities for the positive class
y_pred_prob = pipeline.predict_proba(X_test)[:, 1]

# Calculate the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Calculate the AUC score
auc = roc_auc_score(y_test, y_pred_prob)
print("AUC score: ",auc)

"""### Save the Final Model"""

import pickle

output_file = 'model.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, pipeline), f_out)
print("model saved.")