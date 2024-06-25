# Image Annotation Tool

This repository contains an Image Annotation Tool built using Flask. The tool allows users to upload images or provide image URLs for annotation. The annotated images are displayed on the web page, and users have the option to download them.

## Features

- Upload images for annotation.
- Provide image URLs for annotation.
- Display annotated images on the web page.
- Download annotated images.
- Supports common image formats: JPG, JPEG, PNG.

## Folder Structure

- **ImageAnnotation**: Main folder containing the project files.
  - **static**: Contains static files such as CSS and JavaScript.
  - **templates**: Contains HTML templates for the Flask web application.
  - **uploads**: Contains uploaded and annotated images.
  - **models**: Contains the YOLOv8 segmentation model files.
  - **app.py**: Contains the python script for the website using Flask.

## Getting Started
Example:
![image](https://github.com/SambitSatapathy07/ImageAnnotationTool/assets/167393025/f92e78f7-a24b-4d74-8e20-92d5539213ed)

### Prerequisites

- Python 3.x
- Flask
- OpenCV
- NumPy
- Pillow
- Requests
- Ultralyitcs YOLO

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SambitSatapathy07/ImageAnnotationTool.git
   cd ImageAnnotationTool
