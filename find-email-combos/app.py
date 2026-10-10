import streamlit as st
import csv
from io import StringIO
from components import render_header, render_footer

render_header("Forgot Email Digits Tool")
st.write("""Forgot the last digits of your email?
Just enter the part you remember — this tool will generate all possible email combinations with the digits you forgot, so you can try logging in again.""")
st.html("""
    <h6>You can use <a href="https://app.lumrid.com/" target="_blank">https://app.lumrid.com/</a> later to check if your email is valid or not</h6>
""")

# Inputs
email_prefix = st.text_input("Email prefix", "fredrobinson").replace(" ", "").lower()
email_domain = st.text_input("Email domain", "@gmail.com").replace(" ", "").lower()
digits = st.number_input("How many digits you remember", min_value=1, max_value=5, value=4)
file_type = st.selectbox("File type", ["csv", "txt"])
chunk_size = 1000

# Only generate when user clicks
if st.button("Generate & Show Download Options"):
    limit = 10**digits
    combinations = [f"{email_prefix}{str(i).zfill(digits)}{email_domain}" for i in range(limit)]

    for i in range(0, len(combinations), chunk_size):
        chunk = combinations[i : i + chunk_size]
        filename = f"emails_{i//chunk_size + 1}.{file_type}"

        if file_type == "csv":
            output = StringIO()
            writer = csv.writer(output)
            writer.writerows([[email] for email in chunk])
            data = output.getvalue().encode()
            mime = "text/csv"
        else:
            data = "\n".join(chunk).encode()
            mime = "text/plain"

        st.download_button(
            label=f"📥 Download {filename}", data=data, file_name=filename, mime=mime
        )
# Warning Message
st.html("""
    <div style="color: orange; font-size: 18px; font-weight: bold;">
        ⚠️ <strong>Disclaimer:</strong> This tool is intended for lawful and ethical use only. Please do not use it for any illegal activities.
    </div>
""")

# Footer Section with Links
render_footer("Email Digits Tool")