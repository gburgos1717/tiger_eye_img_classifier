



import streamlit as st #import streamlit

# import tensorflow as tf
from tensorflow.keras.models import load_model

import cv2 # opencv
from PIL import Image, ImageOps # pillow -> PIL(fork)
import numpy as np # numpy


# attempt to forcast errors and ensure code will run  
# st.set_option('depreecation.showfileUploaderEncoding', False)
st.cache(allow_output_mutation=True)


# Load in model and write a header to streamlit page
model = load_model('./saved_model/model_13epoch.hdf5')
st.write(
"""
# Tiger Eye Gemstone Classification
## Red | Blue | Gold
""")


# Create a file uploader and predict images that are uploaded
file = st.file_uploader("Please upload your tiger eye image", type=['png','jpg'])

# predict_image function will upload images and convert them into arrays
# arrays will be viewed as data points for our model to make predictions
def predict_image(data,model):
    size = (200,200) # ensure size is equivalent to size predicted in cnn model
    image = ImageOps.fit(data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...] # reshaping to a 4 dimension array
    predict_img = model.predict(img_reshape)
    return predict_img

# execution flow for our streamlit app
if file is None: # for when there is no image uploaded
    st.text("Please upload an image file. Only 'png' and 'jpg' formats accepted." )
else: # for when an image is uploaded
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = predict_image(image,model)
    tiger_color_class = ['Red Tiger Eye', 'Blue Tiger Eye', 'Gold Tiger Eye']
    output = f' ### The gemstone in this image appears to be... {tiger_color_class[np.argmax(predictions)]}.'
    st.success(output)
