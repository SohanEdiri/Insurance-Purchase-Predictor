from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('best_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        driving_license = int(request.form['driving_license'])
        region_code = int(request.form['region_code'])
        previously_insured = int(request.form['previously_insured'])
        vehicle_age = int(request.form['vehicle_age'])
        vehicle_damage = int(request.form['vehicle_damage'])
        annual_premium = float(request.form['annual_premium'])
        policy_sales_channel = int(request.form['policy_sales_channel'])
        vintage = int(request.form['vintage'])

        # Prepare the feature array for prediction
        features = np.array([[gender, age, driving_license, region_code, 
                              previously_insured, vehicle_age, vehicle_damage, 
                              annual_premium, policy_sales_channel, vintage]])
        
        # Make prediction
        prediction = model.predict(features)
        result = 'Will Purchase Insurance' if prediction[0] == 1 else 'Will Not Purchase Insurance'
        
        return jsonify({'status': 'success', 'prediction': result})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
