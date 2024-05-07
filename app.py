import pickle

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connection_string = 'DRIVER={SQL Server};SERVER=你的服务器地址;DATABASE=你的数据库;UID=你的用户名;PWD=你的密码'

with open("ML_Model_Package.pkl", 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api-predict', methods=['POST'])
def predict():
    data = request.json
    msg = data['inputData']
    try:

        return jsonify(
            {
                'prediction': 'our predictions is: Depressed',
                'message': 'Depressed',
                'article1': 'article1....',
                'article2': 'article2....',
                'article3': 'article3....',

            }), 200
        # with pyodbc.connect(connection_string) as conn:
        #     curses = conn.cursor()asdasdas
        #     return jsonify({'message': 'User added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
