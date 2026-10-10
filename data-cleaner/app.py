import streamlit as st
import pandas as pd
from io import BytesIO
from components import render_header, render_footer

# App title and description
render_header("Data Sweeper")
st.write("Upload CSV or Excel files, clean, transform, edit, and download.")

# File uploader
uploaded_files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        # Determine file type
        ext = file.name.split(".")[-1].lower()
        try:
            if ext == "csv":
                try:
                    # Attempt automatic delimiter detection
                    df = pd.read_csv(file, sep=None, engine="python", on_bad_lines="skip")
                except Exception:
                    file.seek(0)
                    df = pd.read_csv(file, on_bad_lines="skip")
            else:
                df = pd.read_excel(file)
        except Exception as err:
            st.error(f"❌ Failed to parse **{file.name}**: {err}")
            continue
        
        # Show file info and preview with editable dataframe
        st.write(f"**📄 {file.name}** ({file.size / 1024:.2f} KB)")
        df = st.data_editor(df, num_rows="dynamic", key=f"editor_{file.name}")  # Allow users to edit the dataframe
        
        # Data cleaning options
        if st.checkbox(f"Clean Data ({file.name})", key=f"clean_{file.name}"):
            if st.button(f"Remove Duplicates ({file.name})", key=f"dup_{file.name}"):
                df = df.drop_duplicates()
                st.write("✅ Duplicates removed!")
            if st.button(f"Fill Missing Values ({file.name})", key=f"fill_{file.name}"):
                num_cols = df.select_dtypes(include="number").columns
                df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
                st.write("✅ Missing numeric values filled!")
        
        # Column selection
        cols = st.multiselect(f"Select Columns ({file.name})", df.columns, default=df.columns)
        df = df[cols]
        
        # Data visualization
        if st.checkbox(f"Show Chart ({file.name})"):
            st.bar_chart(df.select_dtypes(include='number'))
        
        # File conversion
        fmt = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if fmt == "CSV":
                df.to_csv(buffer, index=False)
                mime, ext = "text/csv", "csv"
            else:
                df.to_excel(buffer, index=False, engine='openpyxl')
                mime, ext = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "xlsx"
            buffer.seek(0)
            st.download_button(f"⬇ Download {file.name} as {fmt}", data=buffer, file_name=f"{file.name}.{ext}", mime=mime)
            
            # Success message
            st.success(f"🎉 Processing complete for {file.name}!")

# Footer Section with Links
render_footer("Data Sweeper")
