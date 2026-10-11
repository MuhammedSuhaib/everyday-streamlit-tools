import streamlit as st
import random, string
from src.components import render_header, render_footer

# Header
render_header("Readable Password Generator")

st.write("Users should input a longer and more descriptive base text for their password, which will result in a more readable and memorable password.")
st.write("Example:")
st.markdown("""
<span>streamlit </span><code style="background-color:#f0f0f0;">uI_&7r3@m1!t</code><span> less readable ❌</span>
""", unsafe_allow_html=True)
st.markdown("<span>Streamlit experts. </span><code>_$7re@m1!t-exp3rt&.</code><span> more readable ✅</span>", unsafe_allow_html=True)

# UI Inputs
col1, col2 = st.columns(2)

with col1:
    input_text = st.text_input("Enter base text for password")

with col2:
    given_length = st.number_input("Minimum length", min_value=5, max_value=50, value=17)

# Button to trigger generation
if st.button("Generate Password"):
    if input_text:
        random_number = random.randint(0, 5)
        length_now = len(input_text)

        valency = max(0, given_length - length_now)
        random_prefixes = random.choices(string.ascii_letters, k=valency)
        input_text = "".join(random_prefixes) + "_" + input_text

        input_text = "3".join(input_text.rsplit("e", 1))
        input_text = "!".join(input_text.rsplit("i"))

        my_str = (
            input_text.replace("a", "@", 1)
            .replace("l", "1", 1)
            .replace("o", "0", 1)
            .replace("s", "&", 1)
            .replace("t", "7", 1)
            .replace("g", "9", 1)
            .replace("S", "$", 1)
            .replace("h", "#", 1)
            .replace(" ", "-", random_number)
            .replace(" ", "_")
        )

        st.success("Your password:")
        st.code(my_str)
    else:
        st.warning("Please enter some base text.")

# Pass strength meter
st.title("Password strength meter")
def check_password_strength():
    if input_password := st.text_input("Check password strength", type="password"):
        strength = 0
        # Fix variable name to `input_password`
        if any(char.isdigit() for char in input_password):
            strength += 1
        if any(char.isupper() for char in input_password):
            strength += 1
        if any(char.islower() for char in input_password):
            strength += 1
        if any(char in string.punctuation for char in input_password):
            strength += 1
        if len(input_password) >= 8:
            strength += 1

        st.progress(min(strength / 5, 1.0))
        st.write("Password strength:", strength, "/ 5")
st.button("Check Password Strength", on_click=check_password_strength())

# Footer
render_footer("Password Generator")
