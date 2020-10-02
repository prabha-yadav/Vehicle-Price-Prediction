from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Engine_Repaired_Overhauling_Yes=0
    if request.method == 'POST':
        Mileage = int(request.form['Mileage'])
        Operating_Weight=float(request.form['Operating_Weight'])
        Gross_Weight=float(request.form['Gross_Weight'])
        Bucket_Capacity=int(request.form['Bucket_Capacity'])
        Engine_Power=int(request.form['Engine_Power'])
        Lifting_Capacity=int(request.form['Lifting_Capacity'])
        Operating_Hours=int(request.form['Operating_Hours'])
        vehicle_age=float(request.form['vehicle_age'])
        prediction=model.predict([[Mileage, Gross_Weight, Operating_Weight, Bucket_Capacity, Engine_Power, Lifting_Capacity, Operating_Hours,vehicle_age, Engine_Repaired_Overhauling_Yes]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)