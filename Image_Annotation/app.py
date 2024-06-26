#1 Import necessary dependencies
from flask import Flask, render_template, request, url_for, send_file, redirect
import os
import cv2
import numpy as np
from ultralytics import YOLO
import io
from PIL import Image
import requests
from io import BytesIO

#2 Flask Application Setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

#3 Function to fetch image from URL
def fetch_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        
        # Extract the filename and remove query parameters if any
        filename = url.split("/")[-1].split("?")[0]

        # If filename doesn't have an extension, add a default one
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            filename += ".jpg"

        # Save the image to a temporary file in the uploads directory
        basepath = os.path.dirname(__file__)
        filename = os.path.basename(url)
        filepath = os.path.join(basepath, app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        return image, filepath
    
    else:
        raise FileNotFoundError("Image URL is not accessible or not in the correct format.")


#4 Function to process image with YOLO model
def process_image(image, model):
    result = model(image)
    annotated_image = result[0].plot()
    annotated_image = Image.fromarray(annotated_image.astype(np.uint8))
    return annotated_image, result

#5 Flask Routes (index Page)
@app.route("/")
def welcome():
    return render_template("index.html")

#6 Flask Routes (Annot Image)
@app.route("/", methods=['GET','POST'])
def annot_img():
    model_path = './models/yolov8m-seg.pt'
    model = YOLO(model_path)

    if request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '':
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            filepath = os.path.join(basepath, app.config['UPLOAD_FOLDER'], f.filename)
            f.save(filepath)
            image = Image.open(filepath)

        elif 'url' in request.form and request.form['url'] != '':
            url = request.form['url']
            try:
                image, filepath = fetch_image_from_url(url)
            except FileNotFoundError as e:
                return str(e)

        else:
            return "No file or URL provided."

        annotated_image, result = process_image(image, model)
        annotated_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'annotated_' + os.path.basename(filepath))
        annotated_image.save(annotated_image_path)

        return render_template("index.html", uploaded_image=os.path.basename(filepath), annotated_image='annotated_' + os.path.basename(filepath))

#7 Serve Uploaded File Route
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#8 Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)
