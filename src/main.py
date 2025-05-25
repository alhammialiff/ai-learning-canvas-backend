from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from service.datasetAnalyzer import readDataset

app = Flask(__name__)
CORS(app)

# ========================================
# API Test Signal - Sole to test receipt of data
#                   from Angular
# ========================================
@app.route('/api/test', methods=['POST'])
def apiTestRoute():
    data = request.get_json()
    response = {
        "message": 400,
        "data": "Test FAIL",
        "timestamp": ""
    }

    if(data["message"] != "Connectivity Test"):

        return response
    
        
    response = {
        "message": 200,
        "data": "Test OK",
        "timestamp": ""
    }

    print(f"Test Request: {response}")

    return jsonify(response)

@app.route('/api/dataset', methods=['POST'])
def readDatasetRoute():

    # Parse API Request and get user-selected dataset name
    requestData = request.get_json() 
    selectedDataset = requestData["data"]["dataset"]

    # Read, parse and retrieve dataset
    responseData = readDataset(selectedDataset)

    # Append dataset into response dictionary
    response = {
        "message": 200,
        "data": responseData.to_dict(orient="records"),
        "timestamp": ""
    }

    # Return JSON Serialized dictionary
    return jsonify(response)

    


if __name__ == "__main__":
    
    app.run(debug=True, port=3000)
    