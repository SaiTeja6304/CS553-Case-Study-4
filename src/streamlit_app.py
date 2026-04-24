import streamlit as st
import requests
from llm import generate_response_api

st.set_page_config(page_title="VLM Chat", page_icon=":robot_face:", layout="wide")
st.title("VLM Chat")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

st.chat_message("assistant").markdown("I am a helpful chatbot to answer your questions about the uploaded image")
    
for role, msg in st.session_state.chat_history:
    st.chat_message(role).markdown(msg)

with st.sidebar:
    # with st.expander("Model Details"):
    st.info("API model: google/gemma-4-31B-it is available for interaction.", icon="ℹ️")
    

image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
st.session_state.uploaded_image = image
if image is not None:
    st.image(image)
query = st.chat_input("Ask a question about the image")

if query:
    if st.session_state.uploaded_image is None:
        st.error("Please upload an image")
    else:
        st.chat_message("user").markdown(query)

        with st.spinner("Processing..."):
            # Convert chat history to a concatenated string 
            chat_history_str = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat_history])
            
            response = generate_response_api(image, query, chat_history_str)
        
        st.chat_message("assistant").markdown(response["response"])
        st.session_state.chat_history.append(("user", query))
        st.session_state.chat_history.append(("assistant", response["response"]))

# streamlit run frontend/src/streamlit_app.py --server.port 7011 --server.address 0.0.0.0