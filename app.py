 import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.set_page_config(page_title="Smart IoT Lab Monitoring", layout="wide")
st.title("🧪 Smart IoT Lab Monitoring System - V2")
st.markdown("Day 2 Upgrade - Live Graph + Buzzer + History")

st.sidebar.header("⚙️ Control Panel")
lab = st.sidebar.selectbox("Select Lab", ["ECE Lab 1", "ECE Lab 2", "Embedded Lab"])
gas_limit = st.sidebar.slider("Gas Alert Limit", 200, 800, 400)
buzzer = st.sidebar.toggle("🔊 Buzzer Sound", value=True)

temp = round(random.uniform(24, 35), 1)
hum = round(random.uniform(45, 80), 1)
gas = random.randint(150, 600)
light = random.randint(100, 900)

if gas > gas_limit:
    st.error(f"🚨 GAS LEAKAGE! Gas: {gas} ppm - Evacuate!")
    if buzzer:
        st.warning("🔊 BUZZER: BEEP... BEEP... BEEP... - Buzzer ON!")
        st.audio("https://www.soundjay.com/buttons/beep-01a.wav")
    else:
        st.info("🔇 Buzzer OFF la irukku - ON pannu!")
elif temp > 32:
    st.warning(f"⚠️ HIGH TEMP! {temp} °C - Check AC!")
else:
    st.success(f"✅ {lab} is SAFE - All Normal")

c1, c2, c3, c4 = st.columns(4)
c1.metric("🌡️ Temperature", f"{temp} °C")
c2.metric("💧 Humidity", f"{hum} %")
c3.metric("🔥 Gas", f"{gas} ppm")
c4.metric("💡 Light", f"{light} lux")

st.subheader("📊 Live Sensor Trends - Day 2")
data = {
    "Time": ["10:00", "10:05", "10:10", "10:15", "10:20", "Now"],
    "Temperature": [26.5, 27.1, 28.0, 27.5, temp-1, temp],
    "Humidity": [60, 62, 65, 63, hum-2, hum],
    "Gas": [200, 220, 250, 300, gas-50, gas]
}
df = pd.DataFrame(data)
fig = px.line(df, x="Time", y=["Temperature", "Humidity", "Gas"], markers=True, title="Lab Sensor Live Graph")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📜 History - Last 6 Readings")
st.dataframe(df, use_container_width=True)
st.caption("Made by Tholkappiyan | V2 - Buzzer + History Added")
