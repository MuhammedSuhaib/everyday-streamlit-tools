import streamlit as st

# Define multi-page application routing structure
# Each page points to its corresponding subfolder script
pages = [
    st.Page(
        "streamlit-apps-suite/app.py",         # Relative file path to the welcome/landing page
        title="Home",                          # Display label in sidebar navigation
        icon=":material/home:",                # Material Symbol icon shown in sidebar
        url_path="home",                       # Unique URL slug (e.g., /home)
        default=True,                          # Default landing page when opening the app
    ),
    st.Page(
        "unit_converter/app.py",               # Unit Converter mini-app
        title="Unit Converter",
        icon=":material/swap_horiz:",
        url_path="unit-converter",             # Unique URL slug (e.g., /unit-converter)
    ),
    st.Page(
        "readable-password-generator/app.py",  # Password Generator mini-app
        title="Password Generator",
        icon=":material/password:",
        url_path="password-generator",         # Unique URL slug (e.g., /password-generator)
    ),
    st.Page(
        "data-cleaner/app.py",                 # Data Sweeper / Cleaner mini-app
        title="Data Sweeper",
        icon=":material/cleaning_services:",
        url_path="data-sweeper",               # Unique URL slug (e.g., /data-sweeper)
    ),
    st.Page(
        "data_encryption/app.py",              # Data Encryption mini-app
        title="Data Encryption",
        icon=":material/lock:",
        url_path="data-encryption",            # Unique URL slug (e.g., /data-encryption)
    ),
    st.Page(
        "find-email-combos/app.py",            # Email Combinations mini-app
        title="Email Combinations",
        icon=":material/mark_email_unread:",
        url_path="email-combinations",          # Unique URL slug (e.g., /email-combinations)
    ),
]

# Initialize navigation with defined pages
pg = st.navigation(pages)

# Set global app configuration (favicon, centered layout)
# Note: page_title is omitted here so the browser tab dynamically shows the active page's title
st.set_page_config(
    page_icon=":material/apps:",
    layout="centered",
)

# Render and execute the selected page
pg.run()
