from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# ========================================
# API Test Signal - Sole to test receipt of data
#                   from Angular
# ========================================
@app.route('/api/test', methods=['POST'])
def echo():
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


if __name__ == "__main__":
    
    app.run(debug=True, port=3000)
    