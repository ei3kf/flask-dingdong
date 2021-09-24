import flask
from flask import Flask, jsonify
  
app = Flask(__name__)
 
@app.route('/ding', methods=['GET'])
def ding_dong():
    return jsonify('dong!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

