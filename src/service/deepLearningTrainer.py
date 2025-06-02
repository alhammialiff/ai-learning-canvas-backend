import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

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
