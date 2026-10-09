import streamlit as st
import csv
from io import StringIO
st.html(
    """<div style="text-align: center; margin-x: 20px; padding: 20px; border: 2px solid #0078D7; border-radius: 15px; background-color: #121212; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
    <h1 style="color: #66c2ff; font-family: 'Arial', sans-serif;">Welcome to My 🔐 Forgot Email Digits Tool</h1>
</div>
"""
)
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
    limit = 10 ** digits
    combinations = [f"{email_prefix}{str(i).zfill(digits)}{email_domain}" for i in range(limit)]

    for i in range(0, len(combinations), chunk_size):
        chunk = combinations[i:i + chunk_size]
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
            label=f"📥 Download {filename}",
            data=data,
            file_name=filename,
            mime=mime
        )
# Warning Message
st.html("""
    <div style="color: orange; font-size: 18px; font-weight: bold;">
        ⚠️ <strong>Disclaimer:</strong> This tool is intended for lawful and ethical use only. Please do not use it for any illegal activities.
    </div>
""")


# Footer Section with Links
st.html(
    """
    <div style="text-align: center; margin-top: 30%; padding: 20px; border-top: 2px solid #0078D7; background-color: #121212; color: #66c2ff;">
        <p>Thank you for using my Tool! 🌟</p>
        <p>Created by 𝔐𝔲𝔥𝔞𝔪𝔪𝔞𝔡 ͯś𝔲𝔥𝔞𝔦𝔟</p>
    </div>
    """)