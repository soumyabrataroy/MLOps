from flask import Flask, request
import pickle

import numpy as np
import tensorflow as tf

import pandas as pd
from tf.keras.models import load_model

cust_model = load_model('customer_behavior_model/1/')

local_scaler = pickle.load(open('sc.pickle','rb'))

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    print(age)
    print(salary)
    
    prediction = cust_model.predict(local_scaler.transform(np.array([[42,50000]])))[:,1]


    return "The prediction from GCP API is {}".format(prediction)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=8005, debug=True)
    
	
	