import joblib
import numpy as np

model = joblib.load('model.pkl')

def preprocess(Open, High, Low, Volume):
    try:
        # تحويل القيم إلى أرقام
        inputs = np.array([[float(Open), float(High), float(Low), float(Volume)]])
        
        # لو عندك StandardScaler تقدر تطبقه هنا قبل التنبؤ
        # inputs = scaler.transform(inputs)
        
        prediction = model.predict(inputs)[0]
        return round(prediction, 2)
    except Exception as e:
        return f"Error: {str(e)}"
