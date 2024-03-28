import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image

def main():
    st.title("Cifar10 Web Classifier")
    st.write('Upload any image you think fits into one of the classes and see if the model predicts correctly')

    file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)

        resized_image = image.resize((32, 32))
        img_array = np.array(resized_image) / 255
        img_array = img_array.reshape(1, 32, 32, 3)

        model = tf.keras.models.load_model('cifar10_model.h5')

        predictions = model.predict(img_array)
        cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos, predictions[0], align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis()
        ax.set_xlabel("Probability")
        ax.set_title("Cifar10 Predictions")

        st.pyplot(fig)
    else:
        st.text("Please upload an image")

if __name__ == "__main__":
    main()