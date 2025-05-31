import pandas as pd
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

def cleanDataset(dataset):

    dataset = dataset.fillna(0)
    print(dataset)
    return dataset


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

    # Define target values (ground truth)
    # target = encodedDataset.iloc[:,-1]
    # target = pd.get_dummies()
    # y = target.to_numpy()

    # Note-to-self: No need to convert y into numpy as it already is one (Line 29)
    #               to_numpy() converts a pandas series into numpy.
    y = target

    return {
        "feature": X,
        "target": y
    }


def createTensorDataSet(featureTargetObject):

    dataset = TensorDataset(torch.tensor(featureTargetObject["feature"]).float(),
                            torch.tensor(featureTargetObject["target"]).float())
    
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    return dataloader


def trainModel(dataloader):

    # Create the model
    model = nn.Sequential(nn.Linear(3,2),
                          nn.Linear(2,1))
    
    # Create the loss and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(10):

        for data in dataloader:

            # Set the gradient to zero
            optimizer.zero_grad()

            # Get feature and target from the data loader
            feature,target = data

            # Run a forward pass
            prediction = model(feature)

            target = target.view(-1, 1)

            # Compute loss and gradients
            loss = criterion(prediction, target)
            loss.backward()

            # Update the parameters
            optimizer.step()

            print("Prediction: {}, Target: {}".format(prediction, target))
