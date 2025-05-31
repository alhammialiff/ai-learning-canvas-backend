import pandas as pd

def readDataset(dataset):
    
    datasetPath = ''

    # Populate path with the correct dataset based on selected dataset name
    match dataset:

        case "iris":

            datasetPath = 'data/iris/iris.data'

        case _:

            datasetPath = 'data/iris/iris.data'

    # TO-DO: TO append attribute names as columns
    df = pd.read_csv(datasetPath)
    print(df.head())
    # ..., names = datasetColumns


    return df

