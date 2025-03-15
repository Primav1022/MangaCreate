from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # 示例数据
    data = {
        'message': 'Hello from Flask!'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True) 