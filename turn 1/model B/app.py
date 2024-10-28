# app.py
import flask
import json

app = flask.Flask(__name__)
data_queue = []

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = flask.request.get_json()
    data_queue.append(data)
    return flask.jsonify({'message': 'Data received'}), 201

if __name__ == '__main__':
    app.run(debug=True)
