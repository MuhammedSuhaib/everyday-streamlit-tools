import streamlit as st
from src.components import render_header, render_footer, TOOLS

# Hero Header
render_header("Streamlit Apps Suite")
st.markdown(
    "Welcome to your all-in-one productivity and utility dashboard. "
    "Select an application from the cards below or use the sidebar navigation to get started."
)
st.divider()

cols = st.columns(2)
for i, app in enumerate(TOOLS):
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