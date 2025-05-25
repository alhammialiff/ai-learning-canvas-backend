import pandas as pd

def readDataset(dataset):
    
    datasetPath = ''
    datasetColumns = []

    # Populate path with the correct dataset based on selected dataset name
    match dataset:

        case "iris":

            datasetPath = 'data/iris/iris.data'
            datasetColumns = [
                "sepal_length", "sepal_width", "petal_length", "petal_width", "class"
            ]       

        case _:

            datasetPath = 'data/iris/iris.data'
            datasetColumns = [
                "sepal_length", "sepal_width", "petal_length", "petal_width", "class"
            ]     
    
    # TO-DO: TO append attribute names as columns
    df = pd.read_csv(datasetPath, names = datasetColumns)
    print(df.head())
    # ...


    return df