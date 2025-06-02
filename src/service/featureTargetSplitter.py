import pandas as pd

def defineFeatureTarget(cleanedDataset):

    # encodedDataset = pd.get_dummies(cleanedDataset, columns=['class'])

    # Define input features
    features = cleanedDataset.iloc[:,1:-1]
    # features = cleanedDataset.drop(columns=['Species'])
    target = cleanedDataset.iloc[:,-1]

    # If target is object or a dtype that precedes with 'category, encode it into integer
    if target.dtype == object or str(target.dtype).startswith("category"):
        
        # Returns encoded target with dtype of ndarray[int]
        target = pd.Categorical(target).codes 

    X = features.to_numpy()

    # Note-to-self: No need to convert y into numpy as it already is one (Line 29)
    #               to_numpy() converts a pandas series into numpy.
    y = target

    return {
        "feature": X,
        "target": y
    }
