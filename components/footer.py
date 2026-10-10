import streamlit as st

# Footer Section with Links
def render_footer(app_name: str) -> None:
    """Render styled footer with dynamic app name and hardcoded author/styling."""

    st.html(f"""   
    <div style="text-align: center; margin-top: 30%; padding: 20px; border-top: 2px solid #0078D7; background-color: #121212; color: #66c2ff;">
    <p>Thank you for using the {app_name}! 🌟</p>
    <p>Created by 𝔐𝔲𝔥𝔞𝔪𝔪𝔞𝔡 ͯś𝔲𝔥𝔞𝔦𝔟</p>
    </div>
    """)
