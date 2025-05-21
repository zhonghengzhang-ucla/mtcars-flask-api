from mtcars_prediction import predict
from flask import Flask, jsonify, request
import json

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def server_is_up():
            return 'server is running\n'

    @app.route('/mtcars_predict', methods=['POST'])
    def start():
        to_predict = request.json

        print(to_predict)
        pred = predict(to_predict)
        return jsonify({'mtg prediction': pred})
    return app

app = flask_app()
app.run(debug=True, host='0.0.0.0', port=5001)