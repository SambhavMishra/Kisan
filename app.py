import tensorflow as tf 
import streamlit as st 
from PIL import Image
from tensorflow import keras
import numpy as np
import pickle
import tensorflow_hub as hub
from keras.models import load_model
from keras.utils import custom_object_scope


st.title("Disease prediction") 
import streamlit as st

options = ['Potato','Corn', 'Rice', 'Wheat', 'Cotton']

selected_option = st.selectbox('Select an option', options)

st.write('You selected:', selected_option)

# =============================== POTATO ============================= #

if selected_option == "Potato":
    try:
        model = load_model('Potato.h5')
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        image = Image.open(uploaded_file)

        # Resize the image to the size expected by the Keras model
        image = image.resize((256, 256))

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Expand the dimensions of the array to match the input shape of the Keras model
        image_array = np.expand_dims(image_array, axis=0)


        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image')

        prediction = model.predict(image_array) 
        assign = {
            0: "Early Blight",
            1: "Healthy",
            2: "Late Blight"
        }
        prob = np.argmax(prediction) 
        st.subheader(f'Most probable disease seems to be "{assign[prob]}"')
        

        try:
            if prob == 0:
                with open("text files/PotatoDisease0.txt", "r",  encoding='utf-8') as f:
                    content = f.readlines()
                    for i in content:
                        st.write(i)
            elif prob == 1:
                        st.write("Your potato is healthy pani dalo khush raho")
            elif prob == 2:
                with open("text files/PotatoDisease1.txt", "r",  encoding='utf-8') as f:
                    content = f.readlines()
                    for i in content:
                        st.write(i)
        except:
            st.write("A solution could not be found please connect to you local agriculture help centre")  
    except:
        st.write("Please select an image")


# =============================== CORN ============================= #

if selected_option == "Corn":
    try:
        model = load_model('corn_vedant.h5')
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        image = Image.open(uploaded_file)

        # Resize the image to the size expected by the Keras model
        image = image.resize((256, 256))

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Expand the dimensions of the array to match the input shape of the Keras model
        image_array = np.expand_dims(image_array, axis=0)


        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image')

        prediction = model.predict(image_array) 
        prob = np.argmax(prediction) 
        st.write(prediction)
        # st.subheader(f'Most probable disease seems to be "{assign[prob]}"')
        

        try:
            with open("text files/CornDisease.txt", "r",  encoding='utf-8') as f:
                content = f.readlines()
                for i in content:
                    st.write(i)
        except:
            st.write("A solution could not be found please connect to you local agriculture help centre")  
    except:
        st.write("Please select an image")


# ================================== RICE ================================== #        

elif selected_option == "Rice":
    try:
        model = load_model("rice_vedant.h5")
        
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        image = Image.open(uploaded_file)

        # Resize the image to the size expected by the Keras model
        image = image.resize((256, 256))

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Expand the dimensions of the array to match the input shape of the Keras model
        image_array = np.expand_dims(image_array, axis=0)


        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image')

        prediction = model.predict(image_array) 
        st.write("prediction: ", prediction)    

        try:
            with open("text files/RiceDisease.txt", "r",  encoding='utf-8') as f:
                content = f.readlines()
                for i in content:
                    st.write(i)
        except:
            st.write("A solution could not be found please connect to you local agriculture help centre")
    except:
        st.write("Please select an image")


# ================================== WHEAT ================================== #

elif selected_option == "Wheat":
    try:
        model = load_model("wheat_vedant.h5")
        
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        image = Image.open(uploaded_file)

        # Resize the image to the size expected by the Keras model
        image = image.resize((224, 224))

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Expand the dimensions of the array to match the input shape of the Keras model
        image_array = np.expand_dims(image_array, axis=0)

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image')

        prediction = model.predict(image_array) 
        st.write("prediction: ", prediction[0])
        try:
            with open("text files/WheatDisease.txt", "r",  encoding='utf-8') as f:
                content = f.readlines()
                for i in content:
                    st.write(i)
        except:
            st.write("A solution could not be found please connect to you local agriculture help centre")
    except:
        st.write("please select an image")


elif selected_option == "Cotton":
    try:
# with open('cotton.pkl', 'rb') as f:
#     model = pickle.load(f)
        model = load_model("Cotton.h5")
        
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        image = Image.open(uploaded_file)

        # Resize the image to the size expected by the Keras model
        image = image.resize((256, 256))

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Expand the dimensions of the array to match the input shape of the Keras model
        image_array = np.expand_dims(image_array, axis=0)


        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image')

        prediction = model.predict(image_array) 
        st.write("prediction: ", prediction)    
        try:
            with open("text files/CottonDisease.txt", "r",  encoding='utf-8') as f:
                content = f.readlines()
                for i in content:
                    st.write(i)
        except:
            st.write("A solution could not be found please connect to you local agriculture help centre")
    except :
        st.write("Please select an image")