# Haar Cascade Object Detection App

This project is a Streamlit-based web application that performs object detection on uploaded images using a Haar Cascade classifier. It highlights detected regions and displays both the original and processed images along with the number of detections.

## Features

- Upload a single image through the browser

- Detect objects using a Haar Cascade XML classifier

- Display the original uploaded image

- Display the processed image with bounding boxes

- Show the total number of detected objects

## How It Works

- ObjectDetection loads a Haar Cascade file (stop_data.xml) and applies it to the grayscale version of the uploaded image

- The detector draws bounding boxes around detected objects

- The processed result and count are returned to the Streamlit interface

## The Streamlit interface displays:

- The original uploaded image

- The number of detected objects

- The processed image with detected regions highlighted
