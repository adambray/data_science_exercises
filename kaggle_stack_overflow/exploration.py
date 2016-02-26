# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:47:28 2016

@author: adambray
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

pd.set_option('display.width', 50)
pd.set_option('display.max_colwidth', 100)


def make_features(filename):
    df = pd.read_csv(filename)
    try:
        df["isOpen"] = df.OpenStatus.map({"open": 1, "not a real question": 0, "not constructive": 0, "off topic": 0, "too localized": 0})
    except: pass

    df['title_length'] = df.Title.apply(len)

    df["createdAt"]    = pd.to_datetime(df.PostCreationDate)
    df["registeredAt"] = pd.to_datetime(df.OwnerCreationDate)
    df["ageOfAccount"] = df.createdAt - df.registeredAt
    df["ageInSec"]     = (df["ageOfAccount"] / np.timedelta64(1, 's')).astype(int)

    df["tag_count"]    = df[["Tag1", "Tag2", "Tag3", "Tag4", "Tag5"]].isnull().sum(axis=1)
    df["tag_count"]    = (-1*df["tag_count"]) + 5

    return df

train = make_features("train.csv")

feature_cols = ['tag_count', 'title_length', 'ReputationAtPostCreation', "OwnerUndeletedAnswerCountAtPostTime"]
X = train[feature_cols]
y = train.isOpen

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)

train['openPredProb'] = logreg.predict_proba(X)[:, 1]
zip(feature_cols, logreg.coef_[0])
y_pred_class = logreg.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)


