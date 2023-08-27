import streamlit as st
import numpy as np
import pickle as pkl
from PIL import Image

loaded_model = pkl.load(open("Saved_model.sav", "rb"))

#creating a function for prediction

def strength_prediction(input_data):
    # # Taking input data
    # input_data = (540, 0.0, 0.0, 162.0, 2.5, 1040.0, 676.0, 28)

    # changing the input data into array
    input_data_in_array = np.asarray(input_data)

    # reshaping the data as we are predicting for one instance
    reshaped_input_data = input_data_in_array.reshape(1,-1)

    prediction = loaded_model.predict(reshaped_input_data)
    print(prediction, "MPa")
    
    return prediction


def main():
    # pic1 = Image.open("logo.jpeg")
    # st.image(pic1, width = 200, channels="RGB")
    st.markdown("<h1 style='text-align: center; color: red;'>DNS Tunnelling Detection</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey;'><i>using Machine Learning<i></h2>", unsafe_allow_html=True)
    # pic = Image.open("con.jpg")
    # st.sidebar.image(pic, caption="Just an Image of Concrete", width= 300,channels="RGB")
    
    # Getting the input data from the user
    dnstype = st.sidebar.selectbox("DNS Type", ("CName","A", "AAAA", "TXT","MX"))
    length = st.sidebar.slider("DNS Info Length", 0, 500)
    info = st.text_input("DNS Info")
    
    # Code for prediction
    result = ""
    
    #Creating a button for prediction
    if st.button("SHOW"):
        result = strength_prediction([dnstype, length, info])
     
    st.success(result)

    st.markdown("<h4 style = 'text_align:center; color:green;'><i>Keep your system secure<i></h4>", unsafe_allow_html=True)
    st.markdown("<h6><marquee>Thank you for visiting us!</marquee></h6>", unsafe_allow_html=True)
    # behavior=scroll direction='left'
if __name__ == "__main__":
    main()