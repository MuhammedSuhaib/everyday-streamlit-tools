import streamlit as st
from src.components import render_header, render_footer

# Alt + Shift + F to format the code
render_header("Unit Converter")
st.title("Choose your units to convert")

# Create four columns
col0, col1, col2, col3 = st.columns(4)

# Add content to the first column
with col0:
    st.header("Input")
    val = st.number_input(
        "Enter the value to convert",
    )

# Add content to the second column
with col1:
    st.header("From")
    frm = st.selectbox("Select Unit From", ["Kilometer", "Meter", "Centimeter"])

# Add content to the third column
with col2:
    st.header("To")
    to = st.selectbox("Select Unit To", ["Meter", "Centimeter", "Kilometer"])

# Add content to the fourth column
with col3:
    st.header("Output")
    # Perform the unit conversion based on selection
    if to == "Kilometer" and frm == "Meter":
        output = val / 1000
    elif to == "Meter" and frm == "Kilometer":
        output = val * 1000
    elif to == "Centimeter" and frm == "Meter":
        output = val * 100
    elif to == "Meter" and frm == "Centimeter":
        output = val / 100
    elif to == "Kilometer" and frm == "Centimeter":
        output = val / 100000
    elif to == "Centimeter" and frm == "Kilometer":
        output = val * 100000
    elif to == frm:
        output = val
    else:
        output = None

    # Display the conversion output
    if output is not None:
        st.html("Conversion Output:" f"""
            <div style="background-color: rgb(38, 39, 48); height: 43px; width: 150px;  display: flex; align-items: center; justify-content: center; border-radius: 10px;">{output} {to}</div>
        """)
    else:
        st.write("Invalid conversion")
with col3:
    st.html("""
    <button style="background-color: #00d3ff36; height: 43px; width: 150px;  display: flex; align-items: center; justify-content: center; border-radius: 10px;">Convert</button>
    """)
# Footer Section with Links
render_footer("Unit Converter")
