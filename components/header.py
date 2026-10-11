import streamlit as st

# Header Section with Links
def render_header(title: str) -> None:
    """Render a styled, responsive header banner with an animated shimmer divider."""
    
    st.html(f"""
    <style>
        @keyframes shimmer {{
            0% {{ background-position: -100% 0; }}
            100% {{ background-position: 200% 0; }}
        }}
        .shimmer-line {{
            height: 1px;
            width: 50%;
            margin: clamp(12px, 3vw, 24px) auto 0;
            background: linear-gradient(90deg, transparent, #ffffff, transparent);
            background-size: 200% 100%;
            animation: shimmer 2.5s linear infinite;
        }}
        .header-container {{
            padding: clamp(24px, 5vw, 48px) clamp(16px, 4vw, 24px);
        }}
        .header-title {{
            font-size: clamp(1.5rem, 5vw, 3rem);
        }}
    </style>
    <div class="header-container" style="
        text-align: center;
        margin: 0 20px;
        border-radius: 16px;
        background: linear-gradient(145deg, #050505 0%, #0a0a0a 100%);
        border: 1px solid #1f1f1f;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    ">
        <div class="header-title" style="
            background: linear-gradient(180deg, #ffffff 0%, #8a8a8a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -0.05em;
            line-height: 1.2;
        ">{title}</div>
        <div class="shimmer-line"></div>
    </div>
    """)
