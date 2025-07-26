# 📈 Stock Price Prediction Web App

A lightweight and interactive web app to predict stock prices using Support Vector Regression (SVR), powered by Flask and deployed using Render.

---

## 🌟 Demo
Live App: https://stock-prediction-p1bx.onrender.com/predict

---

##  Model Summary

The model uses **SVR (Support Vector Regression)** with `rbf` kernel, trained using historical stock data (Open, High, Low, Volume) to predict the **Closing Price**.

###  Final selected parameters:
- `C = 100`
- `gamma = 0.01`
- `kernel = rbf`

Model was selected using `GridSearchCV` and evaluated using **Negative Mean Squared Error**.



