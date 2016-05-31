#! /usr/bin/env python


import numpy as np
import h5py

from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from time import time

def loadData():
    f=h5py.File("../160406/data.h5")
    train_X=f["train_X"][:]
    train_Y=f["train_Y"][:]
    train_Y=(train_Y>4).astype(np.int)
    test_X=f["test_X"][:]
    test_Y=f["test_Y"][:]
    test_Y=(test_Y>4).astype(np.int)
    return train_X,train_Y,test_X,test_Y

def accuracy(y_pred,y_true,classifierName):
    count=np.sum(y_pred==y_true)
    precision=(count*1.0)/(y_pred.shape[0])
    print(classifierName+" : "+str(precision))

def main():
    np.random.seed(0)
    n_folds=10
    verbose=True
    shuffle=True
    train_X,train_Y,test_X,test_Y=loadData()

    if shuffle:
        idx=np.random.permutation(train_Y.shape[0])
        train_X=train_X[idx]
        train_Y=train_Y[idx]

    skf=list(StratifiedKFold(train_Y,n_folds))
    #print(skf)
    clfs=[
            RandomForestClassifier(n_estimators=100,n_jobs=-1,criterion='gini'),
            RandomForestClassifier(n_estimators=100,n_jobs=-1,criterion='entropy'),
            ExtraTreesClassifier(n_estimators=100,n_jobs=-1,criterion='gini'),
            #ExtraTreesClassifier(n_estimators=100,n_jobs=-1,criterion='entropy'),
            #GradientBoostingClassifier(learning_rate=0.05,subsample=0.5,max_depth=7,n_estimators=100)            
            ]
    dataset_blend_train=np.zeros((train_X.shape[0],len(clfs)))
    dataset_blend_test=np.zeros((test_X.shape[0],len(clfs)))

    for j,clf in enumerate(clfs):
        dataset_blend_test_j=np.zeros((test_X.shape[0],len(skf)))
        for i,(train,test) in enumerate(skf):
            K_train_x=train_X[train]
            K_train_y=train_Y[train]
            K_test_x=train_X[test]
            K_test_y=train_Y[test]
            clf.fit(K_train_x,K_train_y)
            y_submission=clf.predict_proba(K_test_x)[:,1]
            dataset_blend_train[test,j]=y_submission
            dataset_blend_test_j[:,i]=clf.predict_proba(test_X)[:,1]
        auc=roc_auc_score(train_Y,dataset_blend_train[:,j])
        print(str(j)+"=:"+str(auc))
        dataset_blend_test[:,j]=dataset_blend_test_j.mean(1)

    print("blending...")
    clf=LogisticRegression()
    clf.fit(dataset_blend_train,train_Y)
    y_submission=clf.predict_proba(dataset_blend_test)[:,1]
    final_auc=roc_auc_score(test_Y,y_submission)
    print("final auc:"+str(final_auc))

if __name__=='__main__':
    main()
