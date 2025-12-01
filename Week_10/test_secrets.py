import streamlit as st

st.title("Test Gemini Secrets Setup")

try:
    api_key = st.secrets["AIzaSyBoX_a2R-iVE9T0hB9HAbajDAua9vAzIxs"]
    st.success("✅ API key loaded successfully!")
    st.write(f"Key starts with: {api_key[:15]}...")
except Exception as e:
    st.error(f"Error loading API key: {e}")
    st.info("Make sure ..streamlit/secrets.toml exists and contains GOOGLE_API_KEY")