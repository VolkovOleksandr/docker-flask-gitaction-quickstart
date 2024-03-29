from flask import Flask, jsonify
from flask_cors import CORS
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-env", type=str, default="dev")

application = Flask(__name__)
application.config['JSON_SORT_KEYS'] = False
CORS(application)

environment = parser.parse_args().env

# Root endpoint
@application.route('/', methods=['GET'])
def root():
    print(f"Environment: {environment}")
    return jsonify({f"Docker - REST APIs - {environment} environment": "v1.0"})

if __name__ == "__main__":
    if environment == "dev":
        application.run(debug=True, host='0.0.0.0', port=5003)
    else:
        from waitress import serve
        serve(application, host="0.0.0.0", port=5000)