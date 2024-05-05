from flask import Flask, request, jsonify

app = Flask(__name__)

connection_string = 'DRIVER={SQL Server};SERVER=你的服务器地址;DATABASE=你的数据库;UID=你的用户名;PWD=你的密码'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    name = data['name']
    msg = data['message']
    try:
        return jsonify({'message': 'User added successfully'}), 200
        # with pyodbc.connect(connection_string) as conn:
        #     curses = conn.cursor()asdasdas
        #     return jsonify({'message': 'User added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
