'''
Date: 2021-07-15 18:20:11
LastEditors: Liuliang
LastEditTime: 2021-07-15 18:21:14
Description: 
'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
