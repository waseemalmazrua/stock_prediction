from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model, scaler = joblib.load('model2025.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        open_ = float(request.form['open'])
        high = float(request.form['high'])
        low = float(request.form['low'])
        volume = float(request.form['volume'])

        input_array = np.array([[open_, high, low, volume]])
        input_scaled = scaler.transform(input_array)  

        prediction = model.predict(input_scaled)[0]  

        return render_template('index.html', prediction=round(prediction, 2))
    except Exception as e:
        return f"<h2>Error: {str(e)}</h2>"


if __name__ == '__main__':
    app.run(debug=True)
