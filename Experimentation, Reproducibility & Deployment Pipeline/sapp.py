import streamlit as st
import requests
import os

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/train-model"

st.set_page_config(page_title="MLOps Model Trainer", page_icon="🤖", layout="centered")

st.title("🤖 MLOps Model Training Dashboard")
st.write("Upload your dataset to train a classification model and view training results.")

uploaded_file = st.file_uploader("📂 Upload CSV file for training", type=["csv"])

if uploaded_file is not None:
    if st.button("🚀 Train Model"):
        with st.spinner("Training model... please wait ⏳"):
            # Send file to FastAPI backend
            files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
            response = requests.post(BACKEND_URL, files=files)

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Model Trained Successfully!")

            st.markdown(f"**Accuracy:** `{result['accuracy']:.4f}`")
            st.markdown(f"**Model Path:** `{result['model_path']}`")
            st.markdown(f"**Report Path:** `{result['report_path']}`")

            # Try to read and display the report content
            report_path = result.get("report_path")
            if report_path and os.path.exists(report_path):
                with open(report_path, "r") as f:
                    report_content = f.read()
                st.text_area("📄 Classification Report", report_content, height=300)
            else:
                st.info("Report file not found on frontend machine (since it's saved on backend).")

        else:
            st.error(f"❌ Error: {response.json().get('detail', 'Unknown error')}")
else:
    st.info("👆 Please upload a CSV file to begin training.")
