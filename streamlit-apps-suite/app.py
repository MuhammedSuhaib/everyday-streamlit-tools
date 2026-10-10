import streamlit as st
from components import render_header, render_footer

# Hero Header
render_header("Streamlit Apps Suite")
st.markdown(
    "Welcome to your all-in-one productivity and utility dashboard. "
    "Select an application from the cards below or use the sidebar navigation to get started."
)

st.divider()

# SaaS-style Grid Layout for App Cards
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🔄 Unit Converter")
        st.write("Easily convert length measurements between Kilometers, Meters, and Centimeters in real-time.")
        st.page_link("unit_converter/app.py", label="Open Unit Converter", icon=":material/swap_horiz:")

    with st.container(border=True):
        st.subheader("🧹 Data Sweeper")
        st.write("Upload CSV/Excel files, clean missing data, remove duplicates, and visualize your dataset.")
        st.page_link("data-cleaner/app.py", label="Open Data Sweeper", icon=":material/cleaning_services:")

    with st.container(border=True):
        st.subheader("✉️ Email Combinations")
        st.write("Generate and export candidate email prefix/digit permutations for account recovery.")
        st.page_link("find-email-combos/app.py", label="Open Email Combinations", icon=":material/mark_email_unread:")

with col2:
    with st.container(border=True):
        st.subheader("🔐 Password Generator")
        st.write("Create readable, memorable passwords based on custom phrases and check password strength.")
        st.page_link("readable-password-generator/app.py", label="Open Password Generator", icon=":material/password:")

    with st.container(border=True):
        st.subheader("🔒 Data Encryption")
        st.write("Encrypt and decrypt sensitive text securely using symmetric Fernet encryption with passkeys.")
        st.page_link("data_encryption/app.py", label="Open Data Encryption", icon=":material/lock:")

# Footer Section with Links
render_footer("Streamlit Apps Suite")
