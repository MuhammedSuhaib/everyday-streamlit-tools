import streamlit as st

# Define multi-page application routing structure
# Each page points to its corresponding subfolder script
pages = [
    st.Page(
        "src/app/streamlit-apps-suite/app.py", # Relative file path to the welcome/landing page
        title="Home",                          # Display label in sidebar navigation
        icon=":material/home:",                # Material Symbol icon shown in sidebar
        url_path="home",                       # Unique URL slug (e.g., /home)
        default=True,                          # Default landing page when opening the app
    ),
    st.Page(
        "src/app/unit_converter/app.py",       # Unit Converter mini-app
        title="Unit Converter",
        icon=":material/swap_horiz:",
        url_path="unit-converter",             # Unique URL slug (e.g., /unit-converter)
    ),
    st.Page(
        "src/app/readable-password-generator/app.py",  # Password Generator mini-app
        title="Password Generator",
        icon=":material/password:",
        url_path="password-generator",         # Unique URL slug (e.g., /password-generator)
    ),
    st.Page(
        "src/app/data-cleaner/app.py",         # Data Cleaner mini-app
        title="Data Cleaner",
        icon=":material/cleaning_services:",
        url_path="data-cleaner",               # Unique URL slug (e.g., /data-cleaner)
    ),
    st.Page(
        "src/app/data_encryption/app.py",      # Data Encryption mini-app
        title="Data Encryption",
        icon=":material/lock:",
        url_path="data-encryption",            # Unique URL slug (e.g., /data-encryption)
    ),
    st.Page(
        "src/app/find-email-combos/app.py",    # Email Combinations mini-app
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

# External tools in sidebar
with st.sidebar:
    st.link_button(
        "Wearable Cheat Notes",
        "https://push-notifcation-splitter.streamlit.app/",
        icon=":material/aod_watch:",
        use_container_width=True,
    )

# Render and execute the selected page
pg.run()
