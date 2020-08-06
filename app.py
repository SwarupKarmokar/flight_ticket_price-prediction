from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
predict_model = pickle.load(open("flight_price.pkl", 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()

    if request.method == 'POST':

        Airline = request.form['Airline']
        if Airline == 'Air Asia':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif Airline == 'Air India':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif Airline == 'GoAir':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif Airline == 'IndiGo':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif Airline == 'Jet Airways':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif Airline == 'Jet Airways Business':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif Airline == 'Multiple carriers':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif Airline == 'Multiple carriers Premium economy':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif Airline == 'SpiceJet':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif Airline == 'Trujet':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif Airline == 'Vistara':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif Airline == 'Vistara Premium economy':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        Source = request.form['Source']

        if Source == 'Banglore':
            temp_array = [1, 0, 0, 0, 0]
        elif Source == 'Chennai':
            temp_array = [0, 1, 0, 0, 0]
        elif Source == 'Delhi':
            temp_array = [0, 0, 1, 0, 0]
        elif Source == 'Kolkata':
            temp_array = [0, 0, 0, 1, 0]
        elif Source == 'Mumbai':
            temp_array = [0, 0, 0, 0, 1]

        Destination = request.form['Destination']
        if Destination == 'Bangalore':
            temp_array = [1, 0, 0, 0, 0, 0]
        elif Destination == 'Cochin':
            temp_array = [0, 1, 0, 0, 0, 0]
        elif Destination == 'Delhi':
            temp_array = [0, 0, 1, 0, 0, 0]
        elif Destination == 'Hyderabad':
            temp_array = [0, 0, 0, 1, 0, 0]
        elif Destination == 'Kolkata':
            temp_array = [0, 0, 0, 0, 1, 0]
        elif Destination == 'New Delhi':
            temp_array = [0, 0, 0, 0, 0, 1]

        Total_Stops = request.form['Total_Stops']
        if Total_Stops == '0.0':
            temp_array = [1, 0, 0, 0, 0]
        elif Total_Stops == '1.0':
            temp_array = [0, 1, 0, 0, 0]
        elif Total_Stops == '2.0':
            temp_array = [0, 0, 1, 0, 0]
        elif Total_Stops == '3.0':
            temp_array = [0, 0, 0, 1, 0]
        elif Total_Stops == '4.0':
            temp_array = [0, 0, 0, 0, 1]



        output = temp_array

        data = np.array([output])
        my_prediction = int(predict_model.predict(data)[0])
        return render_template('index.html', prediction_text='Your ticket price : {}'.format(my_prediction))


if __name__ == '__main__':
    app.run(debug=True)