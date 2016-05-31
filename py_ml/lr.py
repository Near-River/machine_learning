#! /usr/bin/env python

import numpy as np
import h5py

from time import time

from sklearn.linear_model import LogisticRegression
from sklearn import neighbors
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import roc_auc_score

def loadData():
    f=h5py.File("data.h5")
    train_X=f['train_X'][:]
    train_Y=f['train_Y'][:]
    test_X=f['test_X'][:]
    test_Y=f['test_Y'][:]
    return train_X,train_Y,test_X,test_Y


def accurcy(y_pred,y_true,classifierName):
    count=np.sum(y_pred==y_true)
    precision=(count*1.0)/(y_pred.shape[0])
    print(classifierName+" : "+str(precision))


def DT(train_X,train_Y,test_X,test_Y):
    start=time()
    clf=DecisionTreeClassifier(random_state=0)
    clf.fit(train_X[0:1000],train_Y[0:1000])
    y_pred=clf.predict(test_X)
    accurcy(y_pred,test_Y,"DT")
    print("time :"+ str(time()-start))

def KNN(train_X,train_Y,test_X,test_Y):
    start=time()
    knn=neighbors.KNeighborsClassifier()
    knn.fit(train_X[0:1000],train_Y[0:1000])
    y_pred=knn.predict(test_X)
    accurcy(y_pred,test_Y,"KNN")
    print("time :"+ str(time()-start))

def LR(train_X,train_Y,test_X,test_Y):
    start=time()
    train_Y=(train_Y>4).astype(np.int)
    test_Y=(test_Y>4).astype(np.int)
    clf=LogisticRegression()
    clf.fit(train_X,train_Y)
    y_pred=clf.predict(test_X)
    accurcy(y_pred,test_Y,"LR")
    auc=roc_auc_score(test_Y,y_pred)
    print("auc: "+str(auc))
    print("time :"+ str(time()-start))


if __name__=='__main__':
    train_X,train_Y,test_X,test_Y=loadData()
    KNN(train_X,train_Y,test_X,test_Y)
    DT(train_X,train_Y,test_X,test_Y)
    #LR(train_X[0:1000],train_Y[0:1000],test_X,test_Y)
    
