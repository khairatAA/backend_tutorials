#!/usr/bin/python3
import requests
from flask import Flask, jsonify, Response
"""GET and POST basic infomation"""


app = Flask(__name__)

@app.route('/get')
def get_basic_info():
    """GET basic information"""
    return requests.get('https://backend-test-pfm3.onrender.com/about').content


@app.route('/post')
def post_basic_info():
    """POST basic information"""
    my_info = {
        "name": "Khairat Adesina",
        "endpoint_url": "https://backend-ninja-tutorials.onrender.com/",
        "github_url": "https://github.com/khairatAA/backend_tutorials",
        }

    response = requests.post('https://backend-test-pfm3.onrender.com/data', json=my_info)
    return Response(response.content, content_type='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
