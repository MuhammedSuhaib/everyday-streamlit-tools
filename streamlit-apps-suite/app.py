import streamlit as st
from components import render_header, render_footer

# Hero Header
render_header("Streamlit Apps Suite")
st.markdown(
    "Welcome to your all-in-one productivity and utility dashboard. "
    "Select an application from the cards below or use the sidebar navigation to get started."
)
st.divider()

# 'path' must point to the actual Python file inside each folder
APPS = [
    {
        "icon": ":material/swap_horiz:",
        "title": "Unit Converter",
        "desc": "Easily convert length measurements between Kilometers, Meters, and Centimeters in real-time.",
        "path": "unit_converter/app.py",
        "external": False
    },
    {
        "icon": ":material/cleaning_services:",
        "title": "Data Sweeper",
        "desc": "Upload CSV/Excel files, clean missing data, remove duplicates, and visualize your dataset.",
        "path": "data-cleaner/app.py",
        "external": False
    },
    {
        "icon": ":material/mark_email_unread:",
        "title": "Email Combinations",
        "desc": "Generate and export candidate email prefix/digit permutations for account recovery.",
        "path": "find-email-combos/app.py",
        "external": False
    },
    {
        "icon": ":material/password:",
        "title": "Password Generator",
        "desc": "Create readable, memorable passwords based on custom phrases and check password strength.",
        "path": "readable-password-generator/app.py",
        "external": False
    },
    {
        "icon": ":material/lock:",
        "title": "Data Encryption",
        "desc": "Encrypt and decrypt sensitive text securely using symmetric Fernet encryption with passkeys.",
        "path": "data_encryption/app.py",
        "external": False
    },
    {
        "icon": ":material/aod_watch:",
        "title": "Push Notification Splitter",
        "desc": "Split and manage push notifications efficiently.",
        "path": "https://push-notifcation-splitter.streamlit.app/",
        "external": True
    }
]

cols = st.columns(2)
for i, app in enumerate(APPS):
    with cols[i % 2]:
        with st.container(border=True):
            st.subheader(f"{app['icon']} {app['title']}")
            st.write(app['desc'])
            
            if app['external']:
                st.link_button("Launch App", app["path"], type='primary', use_container_width=True)
            else:
                # st.switch_page requires the exact relative file path to work
                st.button(
                    "Launch App", 
                    use_container_width=True, 
                    type="primary", 
                    key=f"btn_{app['title'].replace(' ', '_')}",
                    on_click=lambda p=app['path']: st.switch_page(p)
                )

render_footer("Streamlit Apps Suite")