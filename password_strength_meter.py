import streamlit as st
import random
import string

# ------------------------ App Configuration ------------------------
st.set_page_config(page_title="🔐 Password Generator", page_icon="🔒")
st.title("Strong Password Generator")
st.markdown("""
Welcome! 👋  
Create secure and random passwords with just a click! 🔑  
Choose your preferences below and generate your custom password.
""")

# ------------------------ Password Generator Function ------------------------
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes both uppercase & lowercase letters

    if use_digits:
        characters += string.digits  # Adds 0–9 if selected

    if use_special:
        characters += string.punctuation  # Adds !@#... if selected

    # Create a password of given length
    return ''.join(random.choice(characters) for _ in range(length))

# ------------------------ User Inputs ------------------------
length = st.slider("🔢 Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits (0–9)")
use_special = st.checkbox("Include Special Characters (!, @, #, etc.)")

# ------------------------ Generate & Display ------------------------
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"🔐 Your Generated Password:\n`{password}`")

# ------------------------ Footer ------------------------
st.markdown("---")
st.markdown("Made with 💗 by [**Bisma Shah**](https://github.com/Bisma-Shah)")
