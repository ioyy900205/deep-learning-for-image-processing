'''
Date: 2021-07-15 10:14:40
LastEditors: Liuliang
LastEditTime: 2021-07-15 18:36:35
Description: 
'''
import requests

resp = requests.post("http://localhost:5000/predict22")

print(resp.content)