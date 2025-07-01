import streamlit as st
import pandas as pd
import pickle

# Load model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set judul aplikasi
st.set_page_config(page_title="Prediksi Kematian Pasien Gagal Jantung", layout="centered")
st.title("💓 Prediksi Kematian Pasien Gagal Jantung")
st.write("Masukkan data pasien untuk memprediksi kemungkinan kematian.")

# Form input pengguna
age = st.number_input("Umur (tahun)", 18, 100, 60)
anaemia = st.selectbox("Anaemia", ["Tidak", "Ya"])
creatinine_phosphokinase = st.number_input("Kadar Creatinine Phosphokinase", min_value=10, max_value=8000, value=250)
diabetes = st.selectbox("Diabetes", ["Tidak", "Ya"])
ejection_fraction = st.number_input("Fraksi Ejeksi (%)", 10, 80, 40)
high_blood_pressure = st.selectbox("Tekanan Darah Tinggi", ["Tidak", "Ya"])
platelets = st.number_input("Jumlah Platelet", min_value=25000, max_value=900000, value=250000)
serum_creatinine = st.number_input("Kreatinin Serum", min_value=0.1, max_value=10.0, value=1.0)
serum_sodium = st.number_input("Natrium Serum (mEq/L)", 100, 150, 137)
sex = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
smoking = st.selectbox("Merokok", ["Tidak", "Ya"])
time = st.number_input("Waktu Pemantauan (hari)", 0, 300, 100)

# Konversi input ke format numerik
input_data = pd.DataFrame({
    'age': [age],
    'anaemia': [1 if anaemia == "Ya" else 0],
    'creatinine_phosphokinase': [creatinine_phosphokinase],
    'diabetes': [1 if diabetes == "Ya" else 0],
    'ejection_fraction': [ejection_fraction],
    'high_blood_pressure': [1 if high_blood_pressure == "Ya" else 0],
    'platelets': [platelets],
    'serum_creatinine': [serum_creatinine],
    'serum_sodium': [serum_sodium],
    'sex': [1 if sex == "Laki-laki" else 0],
    'smoking': [1 if smoking == "Ya" else 0],
    'time': [time]
})

# Tombol prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Pasien berisiko **MENINGGAL** dengan probabilitas {probability:.2f}")
    else:
        st.success(f"✅ Pasien kemungkinan **SELAMAT** dengan probabilitas {1 - probability:.2f}")
