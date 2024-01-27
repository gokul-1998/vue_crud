from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import time


app = Flask(__name__)
CORS(app)
studs=json.load(open('students.json'))

@app.route('/api/students', methods=['GET'])
def get_all_students():
    time.sleep(2)
    
    return jsonify(studs)

if __name__ == '__main__':
    app.run(debug=True)