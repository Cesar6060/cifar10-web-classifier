# CIFAR-10 Web Classifier

This project is a web application that allows users to upload an image and classify it using a pre-trained model based on the CIFAR-10 dataset. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class.

## Features

- User-friendly web interface built with Streamlit
- Upload an image and get instant classification results
- Displays the predicted probabilities for each class using a bar chart
- Supports common image formats: JPG, PNG, JPEG

## Installation

1. Clone the repository:
git clone https://github.com/your-username/cifar10-web-classifier.git

2. Install the required dependencies:
pip install numpy matplotlib streamlit tensorflow pillow

3. Download the pre-trained CIFAR-10 model (`cifar10_model.h5`) and place it in the project directory.

## Usage

1. Navigate to the project directory:
cd cifar10-web-classifier

2. Run the Streamlit app:
streamlit run main.py

3. Open a web browser and go to `http://localhost:8501` to access the application.

4. Upload an image that fits into one of the CIFAR-10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, or truck.

5. The application will display the uploaded image and show a bar chart with the predicted probabilities for each class.

## Model

The pre-trained model used in this project is based on the CIFAR-10 dataset and was trained using TensorFlow. The model architecture and training process are not included in this repository. You can replace the `cifar10_model.h5` file with your own trained model if desired.
