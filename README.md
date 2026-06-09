# 🌍 AQI Prediction App

An AI-powered Air Quality Index (AQI) prediction application built with Streamlit and Machine Learning. The app predicts AQI levels based on pollutant concentrations and classifies air quality into easy-to-understand categories.
<img width="1856" height="843" alt="image" src="https://github.com/user-attachments/assets/fd7e17bc-3a2c-493d-bb89-525c5a3e1ce5" />

## 🚀 Features

* 📊 Predict Air Quality Index (AQI) instantly
* 🌫️ Supports multiple pollutant inputs:

  * PM2.5
  * PM10
  * NO
  * NO₂
  * NOx
  * NH₃
  * CO
  * SO₂
  * O₃
* 🤖 Machine Learning-based prediction model
* 🎨 Modern and responsive Streamlit UI
* 📈 Automatic AQI categorization
* ⚡ Real-time predictions

## 🏷️ AQI Categories

| AQI Range | Category    |
| --------- | ----------- |
| 0 – 50    | 😊 Good     |
| 51 – 100  | 🙂 Moderate |
| 101 – 200 | 😟 Poor     |
| Above 200 | 😷 Severe   |

## 🛠️ Tech Stack

* Python
* Streamlit
* NumPy
* Scikit-Learn
* Pickle

## 📂 Project Structure

```bash
AQI_Prediction_App/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. Enter pollutant concentration values.
2. The input data is scaled using a pre-trained scaler.
3. The Machine Learning model predicts the AQI.
4. The predicted AQI is classified into an air quality category.
5. Results are displayed instantly on the dashboard.

## 💻 Installation

```bash
git clone https://github.com/your-username/AQI-Prediction-App.git
cd AQI-Prediction-App

pip install -r requirements.txt
streamlit run app.py
```

## 📊 Input Parameters

| Parameter | Unit  |
| --------- | ----- |
| PM2.5     | μg/m³ |
| PM10      | μg/m³ |
| NO        | μg/m³ |
| NO₂       | μg/m³ |
| NOx       | μg/m³ |
| NH₃       | μg/m³ |
| CO        | mg/m³ |
| SO₂       | μg/m³ |
| O₃        | μg/m³ |

## 🎯 Use Cases

* Environmental Monitoring
* Air Quality Assessment
* Educational Projects
* Data Science & Machine Learning Demonstrations
* Public Health Awareness

## 🔮 Future Enhancements

* Live AQI data integration
* AQI trend visualization
* Location-based predictions
* Interactive pollutant analytics dashboard
* Mobile-friendly enhancements

## 👨‍💻 Author

**Manvey Dhankhar**
B.Tech CSE (AI & ML) | Geeta University

⭐ If you found this project useful, consider giving it a star on GitHub!
