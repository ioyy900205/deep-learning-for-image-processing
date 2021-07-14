'''
Date: 2021-07-14 16:34:09
LastEditors: Liuliang
LastEditTime: 2021-07-14 17:51:18
Description: 
'''
from flask import Flask
app = Flask(__name__)





@app.route('/predict', methods=['POST'])
def predict():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
