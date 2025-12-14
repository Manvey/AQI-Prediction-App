import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


def categorize_aqi(aqi):
    if aqi<=50:
        return "Good 😊"
    elif aqi <=100:
        return "Moderate 🙂"
    elif aqi <=200:
        return "Poor 😟"
    else:
        return "Severe 😷"


st.set_page_config(page_title="AQI Prediction", layout="centered", page_icon="📊")

# Advanced CSS
st.markdown("""
    <style>
    /* 1. Main Background */
    .stApp {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        background-attachment: fixed;
    }

    /* 2. Main Card Container */
    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 3rem !important;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 2rem;
        backdrop-filter: blur(10px);
        max-width: 800px;
        z-index: 100; /* Ensure the main content card is on top */
    }

    /* 3. Typography */
    h1 {
        color: #1abc9c;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .custom-title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    color: #1abc9c;
    margin-bottom: 1rem;
}

    .description-box {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* 4. Input Fields Styling */
    div[data-testid="stNumberInput"] > label {
        color: #2c3e50;
        font-weight: 600;
        font-size: 0.95rem;
    }
    div[data-testid="stNumberInput"] input {
        border-radius: 10px;
        border: 1px solid #d1d5db;
        padding: 0.5rem;
        transition: all 0.3s ease;
    }
    div[data-testid="stNumberInput"] input:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
    }

    /* 5. Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%);
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(56, 239, 125, 0.4);
        color: white;
    }

    /* 6. Result Boxes */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
    }

    /* Hide Streamlit Boilerplate */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Re-enabling or ensuring header is not forcefully hidden, since the custom title is inside the main block. */
    /* header {visibility: hidden;} - REMOVED/COMMENTED OUT */
    </style>
""", unsafe_allow_html=True)

# UI layout

st.markdown("""
<div class="custom-title">📊 AQI Calculator</div>
""", unsafe_allow_html=True)
st.markdown("<div class = 'description-box'>Enter the pollutant values below to calculate the Air Quality Index.</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    pm25 = st.number_input("PM2.5 (μg/m³)", min_value=0, step=1)
    no = st.number_input("NO (μg/m³)", min_value=0, step=1)
    nox = st.number_input("NOx (μg/m³)", min_value=0, step=1)
    co = st.number_input("CO (mg/m³)", min_value=0, step=1)
    o3 = st.number_input("O₃ (μg/m³)", min_value=0, step=1)

with col2:
    pm10 = st.number_input("PM10 (μg/m³)", min_value=0, step=1)
    no2 = st.number_input("NO₂ (μg/m³)", min_value=0, step=1)
    nh3 = st.number_input("NH₃ (μg/m³)", min_value=0, step=1)
    so2 = st.number_input("SO₂ (μg/m³)", min_value=0, step=1)

if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no, no2, nox, nh3, co, so2, o3]])
    input_scaled = scaler.transform(input_data)
    predicted_aqi = round(model.predict(input_scaled)[0], 2)
    category = categorize_aqi(predicted_aqi)

    st.success(f"🌟 **Predicted AQI:** {predicted_aqi}")
    st.info(f" **Air Quality Category:** {category}")
