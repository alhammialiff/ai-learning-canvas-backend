from service.datasetCleaner import cleanDataset, defineFeatureTarget, createTensorDataSet, trainModel


def buildModel(dataset):

    # Clean Dataset
    cleanedDataset = cleanDataset(dataset)

    # Split Feature and Target
    featureTargetSplit = defineFeatureTarget(cleanedDataset)

    # Create a dataloader for training
    dataloader = createTensorDataSet(featureTargetSplit)

    # Train Model
    trainModel(dataloader)