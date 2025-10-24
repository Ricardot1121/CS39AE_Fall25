import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

st.set_page_config(page_title="Live Weather", page_icon="🌡️", layout="wide")

# Disable chart transitions
st.markdown("""
    <style>
      [data-testid="stPlotlyChart"], .stPlotlyChart, .stElementContainer {
        transition: none !important;
        opacity: 1 !important;
      }
    </style>
""", unsafe_allow_html=True)

st.title("🌡️ Live Weather in Denver")
st.caption("Using Open-Meteo API to track temperature and wind speed.")

# --- Auto Refresh Controls ---
st.subheader("🔁 Auto Refresh Settings")
refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)
st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

# --- Weather API Setup ---
lat, lon = 39.7392, -104.9903  # Denver
wurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"

@st.cache_data(ttl=600)
def get_weather():
    try:
        r = requests.get(wurl, timeout=10)
        r.raise_for_status()
        j = r.json()["current"]
        return pd.DataFrame([{
            "time": pd.to_datetime(j["time"]),
            "temperature": j["temperature_2m"],
            "wind": j["wind_speed_10m"]
        }]), None
    except requests.RequestException as e:
        return None, f"Weather API error: {e}"

# --- Session State for History ---
if "weather_history" not in st.session_state:
    st.session_state.weather_history = pd.DataFrame(columns=["time", "temperature", "wind"])

# --- Fetch Weather ---
df, err = get_weather()
if err:
    st.warning(f"{err}\nShowing last known data.")
    df = st.session_state.weather_history.tail(1)

# --- Update History ---
st.session_state.weather_history = pd.concat([st.session_state.weather_history, df]).drop_duplicates(subset="time")

# --- Display Metrics ---
latest = df.iloc[-1]
st.metric("🌡️ Temperature (°C)", f"{latest['temperature']}°")
st.metric("💨 Wind Speed (m/s)", f"{latest['wind']}")

# --- Line Chart of Temperature Over Time ---
st.subheader("📈 Temperature Over Time")
fig = px.line(
    st.session_state.weather_history,
    x="time",
    y="temperature",
    markers=True,
    title="Temperature Trend in Denver",
    labels={"temperature": "°C", "time": "Timestamp"},
    line_shape="spline"
)
st.plotly_chart(fig, use_container_width=True)

if auto_refresh:
    time.sleep(refresh_sec)
    get_weather.clear()
    st.rerun()

