import streamlit as st

# Header Section with Links
def render_header(title: str) -> None:
    """Render a styled header banner with custom title."""

    st.html(f"""
    <div style="
        text-align: center;
        padding: 48px 24px;
        margin: 0 20px;
        border-radius: 16px;
        background: linear-gradient(145deg, #050505 0%, #0a0a0a 100%);
        border: 1px solid #1f1f1f;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    ">
        <div style="
            background: linear-gradient(180deg, #ffffff 0%, #8a8a8a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -0.05em;
            line-height: 1.2;
            ">{title}</div>
        <div style="
            height: 1px;
            width: 50%;
            margin: 24px auto 0;
            background: linear-gradient(90deg, transparent, #2a2a2a, transparent);
        ">
        </div>
    </div>
    """)
