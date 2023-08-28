import streamlit as st
from pycaret.classification import load_model, predict_model
import math
import pandas as pd
from PIL import Image
import base64

# Load the saved PyCaret model
loaded_model = load_model('best_pipeline')

def calculate_entropy(text):
    if not text:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(text.count(chr(x))) / len(text)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def main():
    st.sidebar.image("logo", width= 300,channels="RGB")
    st.sidebar.markdown("""
    <html>
    <head>
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #87CEEB;
        margin: 0;
        padding: 0;
    }
    .fancy-text {
        font-size: 18px;
        line-height: 1.5;
        color: #00008B;
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style> 
    <body>                   
    <p class="fancy-text" >DNS tunnelling is a method used by malicious users who intend to bypass the security gateway to send or receive commands and data. This has a significant impact on revealing or releasing classified information. Taking advantage of the machine learning techniques capabilities, this research aims to adopt a binary classification in order to handle the problem of classifying DNS tunnel which will identify whether the DNS request is either legitimate or tunnelling
    </body>
    </head>
    </html>
    """, unsafe_allow_html=True)
    
    st.markdown(
    """
    <html>
    <head>
    <style>
    h1, h2 {
    margin: 0;
    padding: 0;
    }
    </style>
    <body>
    <h1 style='text-align: center; color: red;'>DNS Tunnelling Detection</h1>
    <h1 style='text-align: center; color: grey;'><i>using Machine Learning<i></h1>
    </body>
    </html>
    """, unsafe_allow_html=True)
    
    # Collect input data from the user
    DNS_type = st.selectbox("DNS_Type", ('CNAME', 'PTR', 'TXT', 'MX', 'A', 'AAAA'))
    DNS_info = st.text_input("DNS_info")
    DNS_Response_Len = st.number_input("DNS_Response_Len:", value=0.0, step=0.1)
    Entropy = calculate_entropy(DNS_info)
    
    # Create a DataFrame with the user input
    user_df = pd.DataFrame({
        'DNS_type': [DNS_type],
        'DNS_info': [DNS_info],
        'DNS_Response_Len': [DNS_Response_Len],
        'Entropy': [Entropy]
    })

    if st.button("Predict"):
        # Use the loaded model to make predictions
        predicted_df = predict_model(loaded_model, data=user_df)
        # Display the entire predicted DataFrame for debugging
        st.write("Predicted DataFrame:", predicted_df)
    st.markdown("<h4 style = 'text_align:center; color:green;'><i>Guardian of Networks: Defend Against Unseen Threats with DNS Tunnel Detection!!!<i></h4>", unsafe_allow_html=True)
    st.markdown("<h6><marquee>Thank you for visiting us!</marquee></h6>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
