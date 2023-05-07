from flask import Flask, jsonify
from flask_cors import CORS
import os

application = Flask(__name__)
application.config['JSON_SORT_KEYS'] = False
CORS(application)

environment = os.getenv('ENV')

# Root endpoint
@application.route('/', methods=['GET'])
def root():
    return jsonify({f"REST APIs - {environment} environment": "v1.0"})

if __name__ == "__main__":
    if environment == "dev":
        application.run(debug=True, host='0.0.0.0', port=5003)
    else:
        application.run(host='0.0.0.0', port=5000)