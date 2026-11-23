import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="Smart IoT Lab Monitoring", layout="wide")
st.title("🧪 Smart IoT Lab Monitoring System")
st.markdown("Live Monitoring of Lab - Temperature, Humidity, Gas & Light")

# Sidebar Control
st.sidebar.header("⚙️ Control Panel")
lab = st.sidebar.selectbox("Select Lab", ["ECE Lab 1", "ECE Lab 2", "Embedded Lab"])
refresh = st.sidebar.slider("Refresh Speed (sec)", 1, 10, 2)
gas_limit = st.sidebar.slider("Gas Alert Limit", 200, 800, 400)

# Fake Live Sensor Data
temp = round(random.uniform(24, 35), 1)
hum = round(random.uniform(45, 80), 1)
gas = random.randint(150, 600)
light = random.randint(100, 900)

# Alert Logic
if gas > gas_limit:
    st.error(f"🚨 GAS LEAKAGE ALERT! Gas Level: {gas} ppm - Evacuate Lab Immediately!")
elif temp > 32:
    st.warning(f"⚠️ HIGH TEMPERATURE! Temp: {temp} °C - Check AC!")
else:
    st.success(f"✅ Lab is SAFE - All Systems Normal - {lab}")

# 4 Big Boxes
col1, col2, col3, col4 = st.columns(4)
col1.metric("🌡️ Temperature", f"{temp} °C", "Normal" if temp < 32 else "HIGH")
col2.metric("💧 Humidity", f"{hum} %", "Good")
col3.metric("🔥 Gas Level", f"{gas} ppm", "DANGER" if gas > gas_limit else "Safe")
col4.metric("💡 Light Intensity", f"{light} lux", "Bright" if light > 400 else "Dim")

# Graph Data
data = {
    "Time": ["10:00", "10:05", "10:10", "10:15", "10:20", "Now"],
    "Temperature": [26.5, 27.1, 28.0, 27.5, temp-1, temp],
    "Humidity": [60, 62, 65, 63, hum-2, hum],
    "Gas": [200, 220, 250, 300, gas-50, gas]
}
df = pd.DataFrame(data)
st.subheader("📊 Live Sensor Trends")
st.line_chart(df.set_index("Time"))

st.subheader("📋 Latest Sensor Data")
st.dataframe(df, use_container_width=True)
st.caption("Made by Tholkappiyan | Smart IoT Lab Monitoring System")
