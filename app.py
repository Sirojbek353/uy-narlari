from flask import Flask, render_template, request
import pickle
import numpy as np

# Flask ilovasini yaratish
app = Flask(__name__)

# Trained modelni yuklash
model = pickle.load(open('asl.pkl', 'rb'))

# Uy sahifasi
@app.route('/')
def home():
    return render_template('index.html')

# Bashorat qilish
@app.route('/predict', methods=['POST'])
def predict():
    # HTML shaklidan ma'lumotlarni olish
    features = [int(request.form['bedrooms']), int(request.form['bathrooms']), int(request.form['sqft_living']),
                int(request.form['sqft_lot']), int(request.form['floors']), int(request.form['waterfront']),
                int(request.form['view']), int(request.form['condition']), int(request.form['sqft_above']),
                int(request.form['sqft_basement']), int(request.form['yr_built']), int(request.form['yr_renovated'])]
    
    # Ma'lumotlarni modelga yuborish va bashorat qilish
    prediction = model.predict([features])[0]
    
    # Natijani HTML sahifasida ko'rsatish
    return render_template('index.html', predicted_price=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
