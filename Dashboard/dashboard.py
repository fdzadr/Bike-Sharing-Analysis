import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

# Menggabungkan path dengan nama file
file_path_day = os.path.join(current_directory, "..", "Bike-sharing-dataset", "day.csv")
file_path_hour = os.path.join(current_directory, "..", "Bike-sharing-dataset", "hour.csv")

# Memuat dataset
df_day = pd.read_csv(file_path_day)
df_hour = pd.read_csv(file_path_hour)

# Konversi kolom 'dteday' ke dalam format datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

st.title("Dashboard Sederhana")

st.subheader("Data Penggunaan Sepeda per Harian (day.csv)")
st.dataframe(df_day)

st.subheader("Statistik Deskriptif day.csv")
st.write(df_day.describe())

st.subheader("Data Penggunaan Sepeda per Jam (hour.csv)")
st.dataframe(df_hour)

st.subheader("Statistik Deskriptif hour.csv")
st.write(df_hour.describe())

st.subheader("Heatmap Korelasi")
numerical_columns = df_day.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df_day[numerical_columns].corr()
st.write(correlation_matrix)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
st.pyplot()

st.subheader("Grafik Jumlah Penggunaan Sepeda per Hari")
st.line_chart(df_day.groupby('dteday')['cnt'].sum())

st.subheader("Rata-rata Penggunaan Sepeda berdasarkan Musim")
st.bar_chart(df_day.groupby('season')['cnt'].sum())

st.subheader("Rata-rata Penggunaan Sepeda per Hari berdasarkan Cuaca")
st.bar_chart(df_day.groupby('weathersit')['cnt'].sum())

st.subheader("Rata-rata Penggunaan Sepeda per Jam berdasarkan Cuaca")
st.bar_chart(df_hour.groupby('weathersit')['cnt'].sum())

st.subheader("Pola Penggunaan Sepeda per Bulan")
pola_penggunaan_sepeda = df_day.groupby('mnth')['cnt'].sum()
st.line_chart(pola_penggunaan_sepeda)

st.subheader("Pola Penggunaan Sepeda per Jam")
pola_penggunaan_sepeda = df_hour.groupby('hr')['cnt'].sum()
st.line_chart(pola_penggunaan_sepeda)

# Menambahkan interaksi dengan pengguna (contoh: slider untuk memilih suhu)
st.sidebar.subheader("Filter Data")
selected_temp = st.sidebar.slider("Pilih Rentang Suhu", min_value=df_day['temp'].min(), max_value=df_day['temp'].max(), value=(df_day['temp'].min(), df_day['temp'].max()))
filtered_data = df_day[(df_day['temp'] >= selected_temp[0]) & (df_day['temp'] <= selected_temp[1])]

# Tampilkan tabel data yang difilter
st.sidebar.subheader("Data yang Difilter")
st.sidebar.write(filtered_data)