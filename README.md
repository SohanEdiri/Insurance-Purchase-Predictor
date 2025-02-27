# Insurance Purchase Prediction - Computational Intelligence Assignment

This web application predicts whether a customer will purchase insurance based on various demographic and behavioral factors. The AI model powering this application is trained using data from the Kaggle competition Playground Series - Season 4, Episode 7: Binary Classification of Insurance Cross-Selling.

---

## 🚀 Features

- Predicts the likelihood of insurance purchase based on customer details.
- User-friendly web interface to input data and get predictions.
- Real-time result display with an option to reset inputs.
- Simple and effective backend using **Flask**.
- Interactive front-end with **Bootstrap**.

---

## 📂 Project Structure

```
├── static                # Contains static files (CSS, JS)
│   ├── css
│   │    └── style.css
│   └── js
│        └── script.js
├── templates             # HTML templates
│   └── index.html
├── best_model.pkl        # Trained machine learning model
├── app.py                # Flask application
├── requirements.txt      # Required Python packages
└── README.md             # Project documentation
```

---

## 📦 Dependencies

- Flask
- numpy
- scikit-learn
- Bootstrap (Frontend)

All dependencies can be installed using the `requirements.txt` file.

---

## 🛠️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insurance-purchase-prediction.git
cd insurance-purchase-prediction
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Access the Application

Open your browser and go to:

```
http://localhost:5000
```

### 5. Make Predictions

- Enter the required input values in the form.
- Click **Proceed** to see the prediction.
- Click **Reset** to clear the form.

---

## ℹ️ Additional Information

- Ensure the `best_model.pkl` file is in the root directory.
- Flask runs on port 5000 by default. Change this if required in `app.py`.

---

## 📷 Screenshots

![Image Alt](https://github.com/SohanEdiri/PII-Detection-System/blob/5f3515a2a778c37f764213534b9c44e6ac8cd604/Screenshot%202025-02-26%20191705.png)

![Image Alt](https://github.com/SohanEdiri/PII-Detection-System/blob/5f3515a2a778c37f764213534b9c44e6ac8cd604/Screenshot%202025-02-26%20192817.png)
