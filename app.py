import cv2
import numpy as np
import streamlit as st
from PIL import Image

class ObjectDetection:
    def __init__(self):
        self.cascade_path = "stop_data.xml"
        self.cascade = cv2.CascadeClassifier(self.cascade_path)
    
    def detect_objects(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        objects = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(20,20))

        for (x, y, w, h) in objects:
            cv2.rectangle(image, (x,y), (x+w, y+h),(255,0,0),2)
        
        return image, len(objects)
    
class ObjectDetectionApp:
    def __init__(self):
        self.detector = ObjectDetection()

    def run(self):
        st.title("Oject detection using Haar Classifier")

        #upload an image
        uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            image_arr = np.array(image) #Converting PIL Image object to numpy array 

            result_image, box_count = self.detector.detect_objects(image_arr)

            st.image(image, caption="Uploaded Image", use_container_width = True)
            
            st.write(f"Detected Objects: {box_count}")
            result_pil = Image.fromarray(result_image)
            st.image(result_pil, caption="Processed Image", use_container_width=True)

if __name__ == "__main__":
    app = ObjectDetectionApp()
    app.run()



